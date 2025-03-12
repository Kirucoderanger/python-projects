print("rate the following qustions from 1 -- 10 :  ")
lone = int(input("how large is the lone? "))
history = int(input("how good is your creadit history? "))
income = int(input("how high is your encome? "))
down_pay = int(input("how large is your down payment? "))

if lone >= 5:
	if history >= 7 and income >= 7:
		print("the decisionis yes")
	if (history >= 7 or income >= 7) and down_pay >= 5:
	print("the decision is yes")
	else:
	print("the decision is no")
		
if lone < 5:
	if history < 4:
		print("the decision is no")
	else:
		if income >= 7 or down_pay >= 7:
			print("the decision is yes")
		if income >= 4 and down_pay >= 4:
			print("the decision is yes")
		else:
			print("the decision is no")
	

	
	