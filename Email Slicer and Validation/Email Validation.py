# Email Validation using String Functions

email = input(" Enter your Email : ") # g@g.in

k,j,d = 0,0,0

if len(email) >= 6: #1
 if email[0].isaplha(): #2
  if ("@" in email) and (email.count()==1): #3
   if (email[-4]==".") ^ (email[-3]=="."): #4
    for i in email:
     if i==i.isspace(): #5
      k=1
     elif i.isalpha():
      if i==i.upper(): # W-- W=W #5
       j=1
     elif i.isdigit():
      continue
     elif i=="_" or i=="." or i =="@":
      continue
     else:
      d=1
    if k==1 or j==1 or d==1:
      print(" Wrong Email 5 ")
    else:
     print(" Right Email ")
   else:
      print(" wrong Email 4 ")
  else:
   print(" Wrong Email 3 ")
 else:
  print(' Wrong Email 2 ')
else:
 print(" Wrong Email 1 ")