metals={
    "Ag" : "Silver",
    "Al" : "Aluminum",
    "Au" : "Gold",
    "Cu" : "Copper",
}

print (metals["Au"])
print (len(metals))


# Example 5  Processing All Items
def main():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students_dict = {
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis", "dav19008@byui.edu", 0],
        "81-298-9238": ["Sama", "Patel", "pat21004@byui.edu", 8]
    }
    # These are the indexes of the elements in the value lists.
    GIVEN_NAME_INDEX = 0
    SURNAME_INDEX = 1
    EMAIL_INDEX = 2
    CREDITS_INDEX = 3
    total = 0
    # For each item in the list add the number
    # of credits that the student has earned.
    for item in students_dict.items():
        key = item[0]
        value = item[1]
        # Retrieve the number of credits from the value list.
        credits = value[CREDITS_INDEX]
        # Add the number of credits to the total.
        total += credits
    print(f"Total credits earned by all students: {total}")
# Call main to start this program.
if __name__ == "__main__":
    main()
    
    # Example 6
def main():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students_dict = {
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis", "dav19008@byui.edu", 0],
        "81-298-9238": ["Sama", "Patel", "pat21004@byui.edu", 8]
    }
    # These are the indexes of the elements in the value lists.
    GIVEN_NAME_INDEX = 0
    SURNAME_INDEX = 1
    EMAIL_INDEX = 2
    CREDITS_INDEX = 3
    total = 0
    # For each item in the list add the number
    # of credits that the student has earned.
    for key, value in students_dict.items():
        # Retrieve the number of credits from the value list.
        credits = value[CREDITS_INDEX]
        # Add the number of credits to the total.
        total += credits
    print(f"Total credits earned by all students: {total}")
# Call main to start this program.
if __name__ == "__main__":
    main()
    
   # Example 4
def main():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students_dict = {
        # student_ID: [given_name, surname, email_address, credits]
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis" "dav19008@byui.edu", 0]
    }
    # These are the indexes of the elements in the value lists.
    GIVEN_NAME_INDEX = 0
    SURNAME_INDEX = 1
    EMAIL_INDEX = 2
    CREDITS_INDEX = 3
    # Get a student ID from the user.
    id = input("Enter a student ID: ")
    # Check if the student ID is in the dictionary.
    if id in students_dict:
        # Find the student ID in the dictionary and
        # retrieve the corresponding value, which is a list.
        value = students_dict[id]
        # Retrieve the student's given name (first name) and
        # surname (last name or family name) from the list.
        given_name = value[GIVEN_NAME_INDEX]
        surname = value[SURNAME_INDEX]
        # Print the student's name.
        print(f"{given_name} {surname}")
    else:
        print("No such student")
# Call main to start this program.
if __name__ == "__main__":
    main()
    
    
    
    
    # Example 7  Converting between Lists and Dictionaries
def main():
    # Create a list that contains five student numbers.
    numbers_list = ["42-039-4736", "61-315-0160",
            "10-450-1203", "75-421-2310", "07-103-5621"]
    # Create a list that contains five student names.
    names_list = ["Clint Huish", "Amelia Davis",
            "Ana Soares", "Abdul Ali", "Amelia Davis"]
    # Convert the numbers and names lists into a dictionary.
    student_dict = dict(zip(numbers_list, names_list))
    # Print the entire student dictionary.
    print("Dictionary:", student_dict)
    print()
    # Convert the student dictionary into
    # two lists named keys and values.
    keys = list(student_dict.keys())
    values = list(student_dict.values())
    # Print both lists.
    print("Keys:", keys)
    print()
    print("Values:", values)
# Call main to start this program.
if __name__ == "__main__":
    main()