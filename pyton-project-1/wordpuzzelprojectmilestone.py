puzzel = "moroni"
turn = 1
guess = input("guess the puzzel word")
while guess != puzzel:
	guess= input ("guess the puzzel word again")
	turn = turn + 1
print ("you guessed it right,", end="")
print (f" it took you {turn} guesses to get the answer")
