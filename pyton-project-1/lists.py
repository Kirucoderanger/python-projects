print("list")
books=[]
books.append("1Nephi")
books.append("2Nephi")
books.append("Jecob")
books.append("Alma")
books.append("Enos")
print ("your books are:")
for book in books:
	print(book)
print()
items=[]
amount=int(input("how many items would you like to purchase"))
for item in range(amount):
 itemss=input("pleas type your item{}:".format(item+1))
 items.append(itemss)
for item in items:
  print(item)
 #print(items)
 # input using a loop.
"""n = int(input("Enter the number of elements: "))
my_list = []
for i in range(n):
element = input("Enter element {}: ". format(i+1))
my_list. append(element)
# Printing the list.
print("List:", my_list)"""