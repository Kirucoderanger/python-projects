num_list = []
new_number = ""

while new_number != 0:
    new_number = int(input("pleas enter number"))
    num_list.append(new_number)
    
total = 0
s_positive = num_list[0]
maximum = num_list[0]
minimum = num_list[0]
for number in num_list:
    total += number
    #if number > maximum:
        #maximum = number
    #elif number < minimum:
        #minimum = number
    if number < s_positive  and number > 0:
        s_positive = number
print (s_positive)
#print (maximum)
#print (minimum)
    
length = len(num_list)
average = total / (length-1)
print (total)
print (average)
print (length)
    
    
