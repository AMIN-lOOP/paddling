import math
import time
import re



Description = (" Greetings and expressing my happiness to start working with you, please contribute to the progress of the collection by honestly answering the questionnaire. ")
print(" ")

print(Description)

print(" ")

fname = input("What is your first and last name?")
if not re.match("^[a-z , " "]*$", fname):
    print ("Only letters a-z allowed!")
    sys.exit()
if len(fname) < 6:
    print ("Please answer correctly")
    sys.exit()

print(" ")

    
age = int(input("How old are you ?"))
if 20 > age:
  print("We apologize for not accepting you in this collection due to your insufficient age.")
  exit()

print(" ")


xp = int(input("How much experience do you have ?"))
if 2 > xp:
  print("We are very sorry, but we apologize for not having enough experience to hire you in this group, and we hope that you will improve yourself in the coming days.")
  exit()
  
print(" ")

familytest1 = input("Do you have a brother or sister ?")
if len(familytest1) > 15:
    print ("Please answer correctly")
    sys.exit()

print(" ")

familytest2 = input("are you married ?")
if not re.match("^[a-z]*$", familytest2):
    print ("Only letters a-z allowed!")
    sys.exit()
 
print(" ")

   
disease = input("Do you have a special disease?")
if not re.match("^[a-z , " "]*$", disease):
    print ("Only letters a-z allowed!")
    sys.exit()
if len(disease) > 2:
    input("Tell us about your disease : ")
    sleep(90)
 
print(" ")

   
skills = input("what skills do you have ?")

print(" ")


familytest4 = input("Do you have a living parent ?")
if not re.match("^[a-z]*$", familytest4):
    print ("Only letters a-z allowed!")
    sys.exit()
if len(familytest4) > 20:
    print ("Please answer correctly")
    sys.exit()

print(" ")


familytest3 = input("Do you have kids ?")
if not re.match("^[a-z]*$", familytest3):
    print ("Only letters a-z allowed!")
    sys.exit()
if len(familytest3) > 2:
    input("Write the ages of your children : ")
    sleep(20)

print(" ")


educationlevel = input("What is your degree ?")

print(" ")


healthlevel = input("do you exercise ?")
if not re.match("^[a-z]*$", healthlevel):
    print ("Only letters a-z allowed!")
    sys.exit()
if len(healthlevel) > 2:
    input("How many hours a week ?")
    sleep(10)






  

