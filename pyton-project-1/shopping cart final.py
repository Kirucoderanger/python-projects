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
		price = float(input("whst is the price of the item you added: "))
		quntity = 0
		while quntity <= 0:
			quntity = int(input("How many quntity did you need: "))
			if quntity <= 0:
				print ("you interd invalid quntity ammount")
				print ()
			else:
				item_list.append(item)
				item_price.append(price)
				item_quntity.append(quntity)
		print ("The item is added to the cart")
		print ()
	elif action == "2":
		print ("The content of your shoping cart are: ")
		hr = "-"
		curuncy = "$"
		print (f"{hr.ljust(75,'-')}")
		print (f"    {'item'}                  {'price'}             {'quty'}           {'sub total'}")
		print (f"{hr.ljust(75,'-')}")
		for i in range (len(item_list)):
			item = item_list[i]
			price = item_price[i]
			quntity = item_quntity[i]
			item_sum = item_price[i] * item_quntity[i]
			print (f"|{i + 1}. {item.ljust(15)}|${price:15.2f}  |  {quntity:10.0f}  |${item_sum:18.2f} |")
   
	elif action == "3":
		exit = len(item_list) + 1
		while exit > len(item_list):
			remove = int(input("Which item number do you want remove: "))
			if remove > len(item_list):
				print ("You enterd invalid item number")
				print ()
			else:
					item_list.pop(remove - 1)
					item_price.pop(remove - 1)
					item_quntity.pop(remove - 1)
					print ("The item is removed successfully")
					print ()
					exit = remove - 1
	elif action == "4":
		total_price = 0
		for i in range (len(item_list)):
			total_price += item_price[i] * item_quntity[i]
		print (f"The total price of items in the shoping cart are: ${total_price:.2f}")
		print ()
	elif action == "5":
		exit = "quit"
	else:
		print ("You enterd invalid choise")
		
	