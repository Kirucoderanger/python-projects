clients = []
clients.append ("kirubel")
clients.append ("mekonen")
clients.append ("lemu")
print (clients)
new_client = ""
num_clients_added = 0
while new_client.lower() != "end":
	print ("if you want quit type END")
	new_client = input ("what is the name of the client?")
	if new_client.lower() == "end":
		print (f"you quit entering clients, you added  {num_clients_added} client to the list")
	else:
		clients.append(new_client)
	num_clients_added = num_clients_added + 1
length_clients = len(clients)
print (f"the list containes {length_clients} clients")
for client in clients:
	print (client)



number_list = []
new_number = ""
num_numbers_added = 0
while new_number.lower() != "end":
	print ("if you want quit type END")
	new_number = input ("what is the number you want to enter to the list? ")
	if new_number.lower() == "end":
		print (f"you quit entering numbers, you added  {num_numbers_added} numbers to the list")
	else:
		number_list.append(new_number)
	num_numbers_added = num_numbers_added + 1
length_number_list = len(number_list)
print (f"the list containes {length_number_list} numbers")
num_total = 0
for number in number_list:
	print (number)
	num_total = float(num_total) + float(number)
print (f"the sum of numbers in the list is {num_total}")
#number = input ("insert numbers to the list")