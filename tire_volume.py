#author:  Kirubel Mekonnen
# Date: 2021-09-26
# Version: 1.0
# Description: This program calculates the volume of a tire and determines the price of the tire based on the volume. The program also asks the user if they would like to purchase the tire and if so, asks for their phone number and writes the tire volume and phone number to a file. The program also writes the tire volume to a file if the user chooses not to purchase the tire. The program also prints the date and time of the calculation.
import math
from datetime import datetime
today = datetime.now()
print("Tire Volume Calculator")
print("This program calculates the volume of a tire.")
print("Please enter the width, aspect ratio, and diameter of the tire in inches.")
width = float(input("Enter the width of the tire in millimeters: "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the wheel in inches: "))
volume = (math.pi * (width**2) * aspect_ratio * ((width * aspect_ratio) + (2540 * diameter))) / 10000000000
print(f"The volume of the tire is {volume:.2f} liters.")
print("Calculation completed on: " + today.strftime("%Y-%m-%d %H:%M:%S"))


if volume >= 40 and volume <= 45:
    print("The Price of the tire is $197.")   
elif volume >= 35 and volume <= 39:
    print("The Price of the tire is $177.")
elif volume >= 30 and volume <= 34:
    print("The Price of the tire is $157.")
elif volume >= 25 and volume <= 29:
    print("The Price of the tire is $137.")
elif volume >= 20 and volume <= 24:
    print("The Price of the tire is $117.")
elif volume >= 15 and volume <= 19:
    print("The Price of the tire is $97.")
elif volume >= 10 and volume <= 14:
    print("The Price of the tire is $77.")  
else:
    print("This volume of tire price not published pleas contact the supplyer directly.")
responce = input("Do you want to buy this volume of tire? (y/n): ")
if responce == "y":
    phone = input("Pleas provied your phone number.")
    with open("volumes.txt", "at") as tire_volumes:
        print (f"{today:%y-%m-%d},{width},{aspect_ratio},{diameter},{volume:.2f},{phone}", sep=" ", end="\n", file=tire_volumes,   flush=False)
    print("thank you for your purchase, your order will processed now.")
else:
    print("Thank you for visiting.")
    with open("volumes.txt", "at") as tire_volumes:
        print (f"{today:%y-%m-%d},{width},{aspect_ratio},{diameter},{volume:.2f}", sep=" ", end="\n", file=tire_volumes,   flush=False)
    
    


