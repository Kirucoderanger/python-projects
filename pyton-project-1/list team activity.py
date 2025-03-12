number_list = []
new_number = ""
num_numbers_added = 0
while new_number != 0:
	print ("if you want quit enter 0")
	new_number = float(input ("what is the number you want to enter to the list? "))
	if new_number == 0:
		print (f"you quit entering numbers, you added  {num_numbers_added} numbers to the list")
	else:
		number_list.append(new_number)
	num_numbers_added = num_numbers_added + 1
length_number_list = len(number_list)
print (f"the list containes {length_number_list} numbers")
num_total = 0
for number in number_list:
	print (number)
	num_total = num_total + number
print (f"the sum of numbers in the list is {num_total}")
num_average = num_total / length_number_list
print (f"the average of the numbers in the list is {num_average}")
largest = number_list[0]
for value in number_list:
	if value > largest:
		largest = value
print (f"the largest number in the list is {largest}")
smallest = number_list[0]
for value in number_list:
		if value < smallest:
			smallest = value
print (f"the smallest number in the list is {smallest}")
smallest_positive =number_list[0]
for value in number_list:
		if value > 0 and value < smallest_positive:
			smallest_positive = value
print (f"the smallest positive number in the list is {smallest_positive}")
sorted_list = sorted(number_list)
for number in sorted_list:
		print (number)
		