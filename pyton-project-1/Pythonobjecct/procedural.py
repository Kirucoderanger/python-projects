from datetime import datetime
# Example 1
def main():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    total = 0
    for x in numbers:
        total += x
    average = total / len(numbers)
    print(f"average: {average:.2f}")
# Call main to start this program.
if __name__ == "__main__":
    main()
    
    
# Example 4
def main():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    numbers.append(78)
    numbers.append(72)
    print(numbers)
# Call main to start this program.
if __name__ == "__main__":
    main()
    
obj = datetime.now()
year = obj.year
new_obj = obj.replace(year=2035)
day_of_week = obj.weekday()
print (new_obj)
print(day_of_week)

# Example 5
def main():
    # Create an empty list that will hold fabric names.
    fabrics = []
    # Add three elements at the end of the fabrics list.
    fabrics.append("velvet")
    fabrics.append("denim")
    fabrics.append("gingham")
    # Insert an element at the beginning of the fabrics list.
    fabrics.insert(0, "chiffon")
    print(fabrics)
    # Get the index where velvet is stored in the fabrics list.
    i = fabrics.index("velvet")
    # Replace velvet with taffeta.
    fabrics[i] = "taffeta"
    print(fabrics)
    # Remove the last element from the fabrics list.
    fabrics.pop()
    # Remove denim from the fabrics list.
    fabrics.remove("denim")
    print(fabrics)
# Call main to start this program.
if __name__ == "__main__":
    main()
    
    """Method	Description
d.clear()	Removes all the elements from the dictionary d.
d.copy()	Returns a copy of the dictionary d.
d.get(key)	Returns the value of the specified key. Calling the get method is almost equivalent to using square brackets ([ and ]) to find a key in a dictionary.
d.items()	Returns a list that contains the key value pairs that are in the dictionary d.
d.keys()	Returns a list that contains the keys that are in the dictionary d.
d.pop(key)	Removes the element with the specified key from the dictionary d.
d.update(other)	Updates the dictionary d with the key value pairs that are in the other dictionary.
d.values()	Returns a list that contains the values that are in the dictionary d.
"""
# Example 6
def main():
    # Create a dictionary with student IDs as
    # the keys and student names as the values.
    students = {
        "42-039-4736": "Clint Huish",
        "61-315-0160": "Amelia Davis",
        "10-450-1203": "Ana Soares",
        "75-421-2310": "Abdul Ali",
        "07-103-5621": "Amelia Davis",
        "81-298-9238": "Sama Patel"
    }
    # Get a student ID from the user.
    id = input("Enter a student ID: ")
    # Lookup the student ID in the dictionary and
    # retrieve the corresponding student name.
    name = students.get(id)
    if name:
        # Print the student name.
        print(name)
        # Remove the student that the user
        # specified from the dictionary.
        students.pop(id)
    else:
        print("No such student")
    print()
    # Use a for loop to print each key value pair
    # in the dictionary. Of course, the code in
    # the body of a loop can do much more with
    # each key value pair than simply print it.
    for key, value in students.items():
        print(key, value)
# Call main to start this program.
if __name__ == "__main__":
    main()
    
#object oriented example    
#variable = object.method(arg1, arg2, ...)
