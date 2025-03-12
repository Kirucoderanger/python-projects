#num = int(input ("pick a random number from 1 - 9:"))
import random
play_again = "yes"
while play_again == "yes":
	turn = 0
	num = random.randint(1, 10)
	gus = ""
	while gus != num:
           
           turn = turn+1
           gus = int(input("what is your guss?"))

           if gus > num:
           	print ("guss lower")
           elif gus < num:
           	print ("guss higher")
           else:
           	
           	print (f"you guseed right the number is {num}")
           	print (f"you have played {turn} turns to get the majic number")
           	play_again = input("Do you want to play again: ")