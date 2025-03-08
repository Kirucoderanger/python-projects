#Outer Kirubel Mekonen
#Purpose CSE 110 project 1: Claver Story
"""
there is additional word(noun) and story in the middel of the pharagraph,
also i used indexing method to distingush the input value (noun) start with vowel or consonant
aoutomaticaly the program will use an "a" if the first index is consonant and "an" if the first index vowel.
"""
print ("Claver Story Maker")
print("pleas enter the following words:")
adjective = input("an adjective:")
animal = input("name of an animal:")
verb1 = input("a verb:")
exclamation = input("an exclamation:")
verb2 = input("a verb:")
noun = input("enter a name of super_bing:")
verb3 = input("a verb:")
#first_letter=noun[0]
output = (f"The other day, I was really in trouble. It all started when i saw a very {adjective} {animal} {verb1} down the hallway.\n'{exclamation.capitalize()}!' I yelled. But all i could think to do was to {verb2} over and over. Miraculously,\n an {noun} came and that caused it to stop, but not before it tried to {verb3} right in front of my family.")
output2 = (f"The other day, I was really in trouble. It all started when i saw a very {adjective} {animal} {verb1} down the hallway.\n'{exclamation.capitalize()}!' I yelled. But all i could think to do was to {verb2} over and over. Miraculously,\n a {noun} came and that caused it to stop, but not before it tried to {verb3} right in front of my family.")
first_letter=noun[0]
if first_letter == "A"  or first_letter == "a" or first_letter == "E" or first_letter == "e" \
      or first_letter == "I" or first_letter == "i" or first_letter == "O" or first_letter == "o"\
      or first_letter == "U" or first_letter == "u" :\
print(output)
else: print(output2)