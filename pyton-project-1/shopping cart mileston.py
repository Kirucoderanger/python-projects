#shoping cart
item_list = []
item_price = []
item_quntity = []
number_of_items = len(item_list)
total_price = 0
exit = ""
print ("welcome to the shoping cart")
while exit != "quit":
	print ("Pleas select one of the following")
	print ("1. Add new item")
	print ("2. View cart")
	print ("3. Remove item")
	print ("4. Compute total")
	print ("5. Quit")
	action = input ("Pleas enter a choies: ")
	if action == "1":
		item = input ("Which item do you like to add: ")
		item_list.append(item)
		print ("The item is added to the cart")
	elif action == "2":
		print ("the content if your shoping cart are:")
		for item in item_list:
			print (item)
	elif action == "5":
		exit = "quit"
	else:
		print ("You enterd invalid choise")
		
	