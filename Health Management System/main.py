print("\t\t\t\t\t\t ------------------------")
print("\t\t\t\t\t\t || THE HEALTH MANAGER ||")
print("\t\t\t\t\t\t ------------------------")
print("\tHello! Save your DIET & EXERCISE here.\n")

while(1):
 answer = int(input("Enter  1:View Saved Data\t\t\t\n2:Add Data\t\t\t\n3:EXIT\n"))
 
 if answer == 3:
  exit(0)

 name = int(input("Press 1 for Navya \t 2 for Helly \t 3 for Aadhya\n"))
 type = int(input("Press 1 for EXERCISE \t 2 for DIET\n"))

 def getdate():
  '''To get the current date and time at time of entry'''
  import datetime
  return(str(datetime.datetime.now()))

  # Reading from the file
  if answer == 1:
   # If the user is Navya
   if name == 1:
    if type == 1:
     try:
      f = open("navya_exer.txt","rt")
      print("\nDetails :")
      print(f.read())
      f.close()
     except:
      print("Details not found")

    elif type == 2:
     try:
      f = open("navya_diet.txt","rt")
      print("\nDetails :")
      print(f.read())
      f.close()
     except:
      print("Details not found")
    else:
     print("\nWRONG INPUT!")

   # If the user is Helly
   elif name == 2:
    if type == 1:
     try:
      f = open("helly_exer.txt","rt")
      print("\nDetails :")
      prit(f.read())
      f.close()
     except:
      print("Details not found")
   elif type == 2:
     try:
      f = open("helly_diet.txt","rt")
      print("\nDetails :")
      print(f.read())
      f.close()
     except:
      print("Details not found")
   else:
     print("\nWRONG INPUT!")
  
  # If the user is Aadhya
  elif name == 3:
   if type == 1:
    try:
     f = open("aadhya_exer.txt","rt")
     print("\nDetails :")
     prit(f.read())
     f.close()
    except:
     print("Details not found")

   elif type == 2:
    try:
     f = open("aadhya_diet.txt","rt")
     print("\nDetails :")
     print(f.read())
     f.close()
    except:
     print("Details not found")
    else:
     print("\nWRONG INPUT!")

#Writing to the file

 if answer == 2:
  #If the user is Navya
  if name == 1:
   if type == 1:
    f = open("navya_exer.txt","at")
    f.write("["+getdate()+"] ")
    f.write(input("Enter exercise you have done : "))
    f.write("\n")
    f.close()
   elif type == 2:
    f = open("navya_diet.txt","at")
    f.write("["+getdate()+"] ")
    f.write(input("Enter diet you have taken : "))
    f.write("\n")
    f.close()
   else:
    print("\nWRONG INPUT!")

 #If the user is Helly
  elif name == 2:
   if type == 1:
    f = open("helly_exer.txt","at")
    f.write("["+getdate()+"] ")
    f.write(input("Enter exercise you have done : "))
    f.write("\n")
    f.close()
   elif type == 2:
    f = open("helly_diet.txt","at")
    f.write("["+getdate()+"] ")
    f.write(input("Enter diet you have taken : "))
    f.write("\n")
    f.close()
   else:
    print("\nWRONG INPUT!")

 #If the user is Aadhya
  elif name == 3:
   if type == 1:
    f = open("aadhya_exer.txt","at")
    f.write("["+getdate()+"] ")
    f.write(input("Enter exercise you have done : "))
    f.write("\n")
    f.close()
   elif type == 2:
    f = open("aadhya_diet.txt","at")
    f.write("["+getdate()+"] ")
    f.write(input("Enter diet you have taken : "))
    f.write("\n")
    f.close()
   else:
    print("\nWRONG INPUT!")


 
