grade = float(input("what is yor grade persentag "))
if grade >= 90:
	print("yuor gread is A")
if grade >= 80 and grade < 90:
	print("yuor grade is B")
if grade >= 70 and grade < 80:
	print("your grade is C")
if grade >= 60 and grade < 70:
	print("your gread is D")
if grade < 60:
	print("your gread is F")
if grade >= 70:
	print("congradulation you pass the class")
else:
	print("you did not pass the class, but you havr another chance ")
	
	
	grade = float(input("what is yor grade persentag "))
remainder = grade % 10
if remainder >= 7 and grade >= 60 and grade < 90:
	sign = "+"
if remainder < 3 and grade >= 60 and grade < 90:
	sign = "-"
if remainder >= 3 and remainder <7 or grade >= 90 or grade < 60:
	sign = ""
if grade >= 90:
	letter = 'A'
if grade >= 80 and grade < 90:
	letter = 'B'
if grade >= 70 and grade < 80:
	letter = 'C'
if grade >= 60 and grade < 70:
	letter = 'D'
if grade < 60:
	letter = 'F'
print (f"your grade is "+letter+sign)
	
if grade >= 70:
	print("congradulation you pass the class")
else:
	print("you did not pass the class, but you havr another chance ")