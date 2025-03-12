child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("what is the price of adult's meal? "))
num_child = int(input("how many childrens are there? "))
num_adult = int(input("how many adults are there? "))
child_sub_total = num_child * child_meal
adult_sub_total = num_adult * adult_meal
sub_total = child_sub_total + adult_sub_total
print (sub_total)
#print (adult_sub_total)
sales_tax = float(input("what is the persentage of sals tax? "))
