import math
import time
"""Unit Converter"""
#variable setting
while True:
    cat = input("Which category would you like to convert? we support length(l) and weight(w):  ")
    if cat == ("l"):
        unit1 = input("Which unit would you like to convert from: ")
        unit2 = input("Which unit would you like to convert to: ")
        num1 = input("Enter your value: " )
    
        ##Calculations  
        if unit1 == "cm" and unit2 == "m":
            ans = float(num1)/100       
        elif unit1 == "mm" and unit2 == "cm":
            ans = float(num1)/10
        elif unit1 == "m" and unit2 == "cm":
            ans = float(num1)*100
        elif unit1 == "cm" and unit2 == "mm":
            ans = float(num1)*10
        elif unit1 == "mm" and unit2 == "m":
            ans = float(num1)/1000
        elif unit1 == "m" and unit2 == "mm":
            ans = float(num1)*1000  
        elif unit1 == "km" and unit2 == "m":
            ans = float(num1)*1000
        elif unit1 == "m" and unit2 == "km":
            ans = float(num1)/1000
        elif unit1 == "mm" and unit2 == "km":
            ans = float(num1)/1000000
        else:
            print("Invalid length unit. Please try again.")
            continue
        print(f"{num1} {unit1} is equal to {round(ans, 2)} {unit2}.")
    elif cat == ("w"):
        unit1 = input("Which unit would you like to convert from: ")
        unit2 = input("Which unit would you like to convert to: ")
        num1 = input("Enter your value: " )
    
        ##Calculations  
        if unit1 == "kg" and unit2 == "g":
            ans = float(num1)*1000
        elif unit1 == "g" and unit2 == "kg":
            ans = float(num1)/1000
        elif unit1 == "kg" and unit2 == "lb":
            ans = float(num1)*2.205
        elif unit1 == "lb" and unit2 == "kg":
            ans = float(num1)/2.205
        elif unit1 == "g" and unit2 == "lb":
            ans = float(num1)/453.592
        elif unit1 == "lb" and unit2 == "g":
            ans = float(num1)*453.592
        else:
            print("Invalid weight unit. Please try again.")
            continue
        print(f"{num1} {unit1} is equal to {round(ans, 2)} {unit2}.")
    else:
        print("Invalid category. Please try again.")
        continue
    choice = input("Do you want to do another conversion? (y/n): ")
    if choice.lower() == "n":
        break
