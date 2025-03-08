print("condition")
loan_size=int(input("how mach loan you want"))
credit=int(input("how good is ypur credit history"))
income=int(input("how high is your income"))
down_payment=int(input("how large is yor down payment"))
should_loan=False
if loan_size >= 5:
	if credit >=7 and income >=7:
		should_loan=True
	elif credit >=7 or income >=7:
		if down_payment >=5:
			should_loan=True
		else:
				should_loan=False
	else:
				should_loan=False
else:
		if credit <4:
			should_loan=False
		else:
				if income >= 7 or down_payment >=7:
					should_loan=True
				elif income >= 4 and down_payment >= 4:
					should_loan=True
				else:
					should_loan=False
if should_loan:
			print("the decision is yes.")
else:
			print("the decisin is no")