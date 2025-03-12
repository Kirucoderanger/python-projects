#wordle, word puzzel game
#autor Kirubel Mekonen Lemu
#the game has five word lists, the game chooses one word randomly for each play
#the game prompt the user to play again with new randomly choosen word at the end
import random
puzzel_list = ["abinadi", "mormon", "lehi", "alma", "adamondiahman"]
play_again = "y"
while play_again.lower() == "y"  :
    turn = 1
    puzzel = random.choice(puzzel_list)
    length = len(puzzel)
    for i in range (length):
     	print ("_", end = " ")
    guess = input ("\nguess the puzzel word: ")
    while puzzel != guess.lower():
        if len(guess) != length:
            print (f"the number of letters you enterd is not equal the number of letters should be {length}")
            guess = input ("guess the puzzel word again: ")
        else:
            for index in range(length):
                letter = guess[index]
                if letter.lower()== puzzel[index]:
                    print (letter.upper() , end = " ")
                elif letter in puzzel:
                    print (letter.lower(), end = " ")
                else:
                    letter = "_"
                    print (letter , end = " ")
            guess = input ("\nguess the puzzel word again: ")
        turn = turn + 1
    print (f"congaradulation you guessed it right, it took you {turn} guess to answer correctly")
    play_again = input ("do you want to play again with another word press Y, to exit press any key ")
