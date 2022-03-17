# Importing libraries

import turtle
import random
import time

# Creating turtle screen
screen = turtle.Screen()
screen.title('SNAKE GAME')
screen.setup(width = 700, height = 700)
screen.tracer(0)
turtle.bgcolor('turquoise')

# Creating a border for our game

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

#Score
score = 0
delay = 0.1

# Snake
snake = turtle.Turtle()
snake.speed()
snake.shape('square')
snake.color("black")
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'

#Food
fruit = turtle.Turtle()
fruit.speed(9)
fruit.shape('circle')
fruit.color('red')
fruit.penup()
fruit.goto(30,30)

old_fruit = []

#Scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("Score :", align="center",font=("Courier",24,"bold"))

###### Define how to move
def snake_go_up():
 if snake.direction != "down":
  snake.direction = "up"

def snake_go_down():
 if snake.direction != "up":
  snake.direction = "down"

def snake_go_left():
 if snake.direction != "right":
  snake.direction = "left"

def snake_go_right():
 if snake.direction != "left":
  snake.direction = "right"

def snake_move():
 if snake.direction == "up":
  y = snake.ycorner()
  snake.sey(y + 20)

 if snake.direction == "down":
  y = snake.ycorner()
  snake.sety(y - 20)

 if snake.direction == "left":
  x = snake.xcorner()
  snake.setx(x - 20)

 if snake.direction == "right":
  x = snake.xcorner()
  snake.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onekeypress(snake_go_up, "Up")
screen.onekeypress(snake_go_down, "Down")
screen.onekeypress(snake_go_left, "Left")
screen.onekeypress(snake_go_right, "Right")

# Main Loop

while True:
 screen.update()
 # snake and fruit collisions
 if snake.distance(fruit) < 20:
  x = random.randint(-290,270)
  y = random.randint(-240,240)
  fruit.goto(x,y)
  scoring.clear()
  score+=1
  scoring.write("Score:{}".format(score),align="center",font=("Courier",24,"bold"))
  delay -= 0.001

  ## Creating new_ball
  new_fruit = turtle.Turtle()
  new_fruit.speed(0)
  new_fruit.shape('square')
  new_fruit.color('red')
  new_fruit.penup()
  old_fruit.append(new_fruit)

# Adding ball to snake

 for index in range(len(old_fruit)-1,0,-1):
  a = old_fruit[index-1].xcorner()
  b = old_fruit[index-1].ycorner()

  old_fruit[index].goto(a,b)

 if len(old_fruit) > 0:
  a = snake.xcorner()
  b = snake.ycorner()
  old_fruit[0].goto(a,b)
 snake_move()

 ## Snake and Border Collision
 
 if snake.xcorner() > 280 or snake.xcorner() < -300 or snake.ycorner() > 240 or snake.ycorner() < -240:
  time.sleep(1)
  screen.clear()
  screen.bgcolor('turquoise')
  scoring.goto(0,0)
  scoring.write(" GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))

 ## Snake Collision

 for food in old_fruit:
  if food.distance(snake) < 20:
   time.sleep(1)
   screen.clear()
   screen.bgcolor('turquoise')
   scoring.goto(0,0)
   scoring.write(" GAME SCORE \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))
   
   time.sleep(delay)

 turtle.Terminator()