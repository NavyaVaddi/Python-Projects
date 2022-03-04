#There are a number of functions that this program requires so let us have an overview of each.

# A random function: to generate rock, paper, or scissors. 
# valid function: to check the validity of the move.
# result function: to declare the winner of the round.
# scorekeeper: to keep track of the score.

# The program requires the user to make the first move before it makes one the move. Once the move is validated the input is evaluated, the # input entered could be a string or an alphabet. After evaluating the input string a winner is decided by the result function and the score of the round is updated by the scorekeeper function. ##

import random
import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or  Scissors? ").capitalize()
    ## Conditions of Rock,Paper and Scissors
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpu_score+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cpu_score+=1
        else:
            print("You win!", player, "covers", computer)
            player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            cpu_score+=1
        else:
            print("You win!", player, "cut", computer)
            player_score+=1
    elif player=='End':
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Plaer:{player_score}")
        break
