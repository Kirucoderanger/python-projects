employee_txt = open("/storage/emulated/0/pythonexersis/hr_system.txt")
#print (name_txt)
for line in employee_txt:
	print (line )
employee_txt.close()


with open ("/storage/emulated/0/pythonexersis/hr_system.txt") as employee_txt:
	for line in employee_txt:
		print (line)
	print ("the file is closed now")
with open ("/storage/emulated/0/pythonexersis/hr_system.txt") as employee_txt:
	for employee_list in employee_txt:
		employee_list = employee_list.split()
		print (employee_list)
		#print (employee_list[0])
with open ("/storage/emulated/0/pythonexersis/hr_system.txt") as employee_txt:
	for employee_list in employee_txt:
		employee_list = employee_list.split()
		#print (employee_list)
		print (employee_list[0])
with open ("/storage/emulated/0/pythonexersis/hr_system.txt") as employee_txt:
	for employee_list in employee_txt:
		employee_list = employee_list.split()
		#print (employee_list)
		print (f"name: {employee_list[0]} ,  title: {employee_list[2]}")

with open ("/storage/emulated/0/pythonexersis/hr_system.txt") as employee_txt:
	for employee_list in employee_txt:
		employee_list = employee_list.strip()
		splited_employee_list = employee_list.split()
		#print (employee_list)
		print (f"name: {splited_employee_list[0]} ,  title: {splited_employee_list[2]}")
		
with open ("/storage/emulated/0/pythonexersis/hr_system.txt") as employee_txt:
	for employee_list in employee_txt:
		employee_list = employee_list.strip()
		splited_employee_list = employee_list.split()
		#print (employee_list)
		salary = float(splited_employee_list[3])
		print (f"{splited_employee_list[0]}  (ID: {splited_employee_list[1]}) , {splited_employee_list[2]}  -   ${salary:.2f}    ")


with open ("/storage/emulated/0/pythonexersis/hr_system.txt") as employee_txt:
	for employee_list in employee_txt:
		employee_list = employee_list.strip()
		splited_employee_list = employee_list.split()
		#print (employee_list)
		salary = float(splited_employee_list[3])
		if splited_employee_list[2] == "Engineer":
			paycheck = salary / 24 +1000
		else:
			paycheck = salary / 24 
		print (f"{splited_employee_list[0]}  (ID: {splited_employee_list[1]}) , {splited_employee_list[2]}  -   ${paycheck:.2f}    ")
	