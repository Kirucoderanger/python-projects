string = "commitment"
print(string)
word = input("choose your favorite latter from the above worf")


string_len = len(string)
print ("your favorite latter is: "+ word.capitalize())
for index in range(string_len):
	letter = string[index]
	if word.lower() == letter:
		#print(letter.upper(), end ="")
		#print(letter.capitalize(), end ="")
		letter = "_"
		print (letter, end = "")
	else: 
	        print (letter, end = "")
	        
	         
	index = index + 1