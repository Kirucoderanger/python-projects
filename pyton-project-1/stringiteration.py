print ("for loop string")
first_name="Brigham"
for letter in first_name:
	print(f"the letter is: {letter}")
print()	
forth_letter=first_name[3]
print (forth_letter)
print()
length=len(first_name)
print(f"your name has", length, "letters")
print()
for index in range(length):
     print (index)
print()
for index in range(length):
 first_name1=first_name[index]
 print (f"Index:{index}   letter:{first_name1}")
 #enumerate
print() 
for i, letter in enumerate(first_name):
 	print(f"The letter {letter} is at position {i}")
print()
fevorite=input("what is your fevorite letter: ")
print()
for letter1 in first_name:
	if letter1.lower()==fevorite.lower():
		print(letter1.upper(), end="")
	else: print(letter1.lower(), end="")
print()
print()
for letter in first_name:
	if letter.lower()==fevorite.lower():
		print("_", end="")
	else:
		print(letter.lower(), end="")
print()