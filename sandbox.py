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
print(f"{today:%Y-%m-%d}")
'''with open("volume.txt", "w") as file:
    file.write(f"Volume: {volume:.2f} liters\n")
    file.write(f"Calculation completed on: {today.strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write(f"{today:%Y-%m-%d}\n")

    with open("volume.txt", "a") as file:
    file.write(f"Volume: {volume:.2f} liters\n")
    file.write(f"Calculation completed on: {today.strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write(f"{today:%Y-%m-%d}\n")'''
    
with open("volumes.txt", "at") as tire_volumes:
    print (f"{today:%y-%m-%d},{width},{aspect_ratio},{diameter},{volume:.2f}", sep=" ", end="\n", file=tire_volumes,   flush=False)
    



