# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

def make_full_name(given_name, family_name):
    """Return a string in this form "family_name; given_name". For
    example, if this function were called like this:
    make_full_name("Sally", "Brown"), it would return "Brown; Sally".

    Parameters
        given_name: a string that contains a person's given name
        family_name: a string that contains a person's family name
    Return: a string in the form "family_name; given_name"
    """
    full_name = f"{family_name}; {given_name}"
    return full_name


def extract_family_name(full_name):
    """Extract and return the family name from a string in this form:
    "family_name; given_name". For example, if this function were
    called like this:
    extract_family_name("Brown; Sally"), it would return "Brown".

    Parameter:
        full_name: a string in the form "family_name; given_name"
    Return: a string that contains a person's family name
    """
    # Find the index where "; " appears within the full name string.
    semicolon_index = full_name.index("; ")

    # Extract a substring from the full name and return it.
    family_name = full_name[0 : semicolon_index]
    return family_name


def extract_given_name(full_name):
    """Extract and return the given name from a string in this form:
    "family_name; given_name". For example, if this function were
    called like this:
    extract_given_name("Brown; Sally"), it would return "Sally".

    Parameter:
        full_name: a string in the form "family_name; given_name"
    Return: a string that contains a person's given name
    """
    # Find the index where "; " appears within the full name string.
    semicolon_index = full_name.index("; ")

    # Extract a substring from the full name and return it.
    given_name = full_name[semicolon_index + 2 : ]
    return given_name




# Example 6
def main():
    sum = 0
    # Get ten or fewer numbers from the user and
    # add them together.
    for i in range(10):
        number = float(input("Please enter a number: "))
        if number == 0:
            break
        sum += number
    # Print the sum of the numbers for the user to see.
    print(f"sum: {sum}")
# Call main to start this program.
if __name__ == "__main__":
    main()
    
    
    
    
    # Example 8 compaund list
def main():
    # These are the indexes of each
    # element in the inner lists.
    YEAR_PLANTED_INDEX = 0
    HEIGHT_INDEX = 1
    GIRTH_INDEX = 2
    FRUIT_AMOUNT_INDEX = 3
    # Create a compound list that stores inner lists.
    apple_tree_data = [
        # [year_planted, height, girth, fruit_amount]
        [2012, 2.7, 3.6, 70.5],
        [2012, 2.4, 3.7, 81.3],
        [2015, 2.3, 3.6, 62.7],
        [2016, 2.1, 2.7, 42.1]
    ]
    # Retrieve one inner list from the compound list.
    one_tree = apple_tree_data[2]
    # Retrieve one value from the inner list.
    height = one_tree[HEIGHT_INDEX]
    # Print the tree's height.
    print(f"height: {height}")
# Call main to start this program.
if __name__ == "__main__":
    main()
    
    # Example 9 compund list with for loop
def main():
    # These are the indexes of each
    # element in the inner lists.
    YEAR_PLANTED_INDEX = 0
    HEIGHT_INDEX = 1
    GIRTH_INDEX = 2
    FRUIT_AMOUNT_INDEX = 3
    # Create a compound list that stores inner lists.
    apple_tree_data = [
        # [year_planted, height, girth, fruit_amount]
        [2012, 2.7, 3.6, 70.5],
        [2012, 2.4, 3.7, 81.3],
        [2015, 2.3, 3.6, 62.7],
        [2016, 2.1, 2.7, 42.1]
    ]
    total_fruit_amount = 0
    # This loop will repeat once for each inner list
    # in the apple_tree_data compound list.
    for inner_list in apple_tree_data:
        # Retrieve the fruit amount from
        # the current inner list.
        fruit_amount = inner_list[FRUIT_AMOUNT_INDEX]
        # Print the fruit amount for the current tree.
        print(fruit_amount)
        # Add the current fruit amount to the total.
        total_fruit_amount += fruit_amount
    # Print the total fruit amount.
    print(f"Total fruit amount: {total_fruit_amount:.1f}")
# Call main to start this program.
if __name__ == "__main__":
    main()



# Example 12  Pass by Value and Pass by Reference
def main():
    print("main()")
    x = 5
    lx = [7, -2]
    print(f"Before calling modify_args(): x {x}  lx {lx}")
    # Pass one integer and one list
    # to the modify_args function.
    modify_args(x, lx)
    print(f"After calling modify_args():  x {x}  lx {lx}")
def modify_args(n, alist):
    """Demonstrate that the computer passes a value
    for integers and passes a reference for lists.
    Parameters
        n: A number
        alist: A list
    Return: nothing
    """
    print("   modify_args(n, alist)")
    print(f"   Before changing n and alist: n {n}  alist {alist}")
    # Change the values of both parameters.
    n += 1
    alist.append(4)
    print(f"   After changing n and alist:  n {n}  alist {alist}")
# Call main to start this program.
if __name__ == "__main__":
    main()