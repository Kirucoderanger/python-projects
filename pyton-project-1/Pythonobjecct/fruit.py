def main():
  # Create and print a list named fruit.
  fruit_list = ["pear", "banana", "apple", "mango"]
  print(f"original: {fruit_list}")
  fruit_list.reverse()
  print(f"reversed: {fruit_list}")
  fruit_list.append("Orange")
  print(f"appended: {fruit_list}")
  
  fruit_list.insert(fruit_list.index("apple"), "cherry")
  print(f"inserted: {fruit_list}")
  fruit_list.remove("banana")
  print(f"removed: {fruit_list}")
  fruit_list.pop()
  print(f"popped: {fruit_list}")
  fruit_list.sort()
  print(f"sorted: {fruit_list}")
  fruit_list.clear()
  print(f"cleared: {fruit_list}")
main()
# Example 1
def main():
    # Create a dictionary with student IDs as
    # the keys and student names as the values.
    students_dict = {
        "42-039-4736": "Clint Huish",
        "61-315-0160": "Amelia Davis",
        "10-450-1203": "Ana Soares",
        "75-421-2310": "Abdul Ali",
        "07-103-5621": "Amelia Davis"
    }
    # Add an item to the dictionary.
    students_dict["81-298-9238"] = "Sama Patel"
    # Remove an item from the dictionary.
    students_dict.pop("61-315-0160")
    # Get the number of items in the dictionary.
    students_dict.c
    length = len(students_dict)
    print(f"length: {length}")
    # Print the entire dictionary.
    print(students_dict)
    print()
    # Get a student ID from the user.
    id = input("Enter a student ID: ")
    # Check if the student ID is in the dictionary.
    if id in students_dict:
        # Find the student ID in the dictionary and
        # retrieve the corresponding student name.
        name = students_dict[id]
        # Print the student's name.
        print(name)
    else:
        print("No such student")
# Call main to start this program.
if __name__ == "__main__":
    main()