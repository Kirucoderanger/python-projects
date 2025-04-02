import os
import sys

# Ensure the script works with the file in the same directory
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "testfile.txt")
# Example 1
def main():
    # Read the contents of a text file
    # named plants.txt into a list.
    text_list = read_list("./testfile.txt")
    #Print the entire list.
    #print(text_list)
    # Print each element of the list one by one.
    for line in text_list:
        print(line, end="")
def read_list(filename="testfile.txt"):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.
    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list that will store
    # the lines of text from the text file.
    text_list = []
    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(file_path, "rt") as text_file:
        # Read the contents of the text
        # file one line at a time.
        for line in text_file:
            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()
            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line + "\n")  # Add a new line for every line of the text.
    return text_list
# Call main to start this program.
if __name__ == "__main__":
    main()
    
    
"""#Writing into a Text File
# Example 1
csv_file_path_quotes = os.path.join(os.path.dirname(__file__), "quotes.csv")
def main():
    # Ask the user to enter a quote.
    quote = input("Please enter an inspirational quote: ")
    # Open the quotes.txt file for appending text.
    with open(csv_file_path_quotes, "at") as quotes_file:
        # Print the quote to the text file.
        print(quote, file=quotes_file)
    #def read_list(filename):
        Read the contents of a text file into a list and return the list.
        with open(csv_file_path_quotes, "rt") as file:
            return file.readlines()
        for line in quotes_file:
                print(line, end="")
    
    def main():
        # Ask the user to enter a quote.
        quote = input("Please enter an inspirational quote: ")
        # Open the quotes.txt file for appending text.
        with open(csv_file_path_quotes, "at") as quotes_file:
            # Print the quote to the text file.
            print(quote, file=quotes_file)
        
        # Read the contents of the file into a list.
        text_list = read_list("./testfile.txt")
        # Print the entire list.
        # print(text_list)
        # Print each element of the list one by one.
        for line in text_list:
            print(line, end="")
# Call main to start this program.
if __name__ == "__main__":
    main()
    
# Example 1
def main():
    # Ask the user to enter a quote.
    quote = input("Please enter an inspirational quote: ")
    # Open the quotes.txt file for appending text.
    with open("quotes.txt", "at") as quotes_file:
        # Print the quote to the text file.
        print(quote, file=quotes_file)
        text_list = read_list("./quotes.txt")
        for line in text_list:
            print(line, end="")
# Call main to start this program.
if __name__ == "__main__":
    main()"""
    
txt_file_path_quotes = os.path.join(os.path.dirname(__file__), "quotes.txt")   
def write_quote_to_file():
        """Accepts user input and writes it to quotes.txt."""
        # Ask the user to enter a quote.
        quote = input("Please enter an inspirational quote: ")
        # Open the quotes.txt file for appending text.
        with open(txt_file_path_quotes, "at") as quotes_file:
            # Write the quote to the text file.
            quotes_file.write(quote + "\n")
            print("Quote saved to quotes.txt.")
            


write_quote_to_file()

def print_quotes_from_file():
    """Reads and prints each line from quotes.txt."""
    with open(txt_file_path_quotes, "rt") as quotes_file:
        for line in quotes_file:
            print(line, end="")

# Call the function to print the quotes
print_quotes_from_file()



# Example 2
def main():
    # Create a list that contains types of small boats.
    boat_list = ["canoe", "kayak", "skiff", "dinghy"]
    # Write the list to a file named small_boats.txt
    write_list("small_boats.txt", boat_list)
def write_list(filename, text_list):
    """Write the contents of a list into a text file.
    Parameters
        filename: the name of the text file to write
        text_list: the list to write to the text file
    Return: nothing
    """
    # Open the text file for writing and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "wt") as text_file:
        # Print the contents of the list into
        # the text file, one line at a time.
        for element in text_list:
            print(element, file=text_file)
# Call main to start this program.
if __name__ == "__main__":
    main()
    
# Example 3
import csv
def main():
    heading_list = ["Title", "Author", "Composer"]
    # Create a compound list of hymns.
    hymns_list = [
        ["O Holy Night", "John Dwight", "Adolphe Adam"],
        ["Oh, Come, All Ye Faithful", "John Wade", "John Wade"],
        ["Joy to the World", "Isaac Watts", "George Handel"],
        ["With Wondering Awe", "Anonymous", "Anonymous"]
    ]
    # Call the write_compound_list function which will
    # write the list of hymns to a file named "hymns.csv".
    write_compound_list("hymns.csv", hymns_list, heading_list)
def write_compound_list(filename, compound_list,
        heading_list=None):
    """Write the contents of a compound list into a CSV file.
    Parameters
        filename: the name of the CSV file to write
        compound_list: the list to write to the CSV file
        heading_list: a list that contains the column headings.
            If heading_list is None, this function will not
            write headings to the CSV File.
    Return: nothing
    """
    # Open the text file for writing and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "wt", newline="") as csv_file:
        # Use the csv module to create a writer object
        # that will write to the opened CSV file.
        writer = csv.writer(csv_file)
        # Write the heading_list to the CSV file.
        if heading_list is not None:
            writer.writerow(heading_list)
        # Write the contents of the list into
        # the CSV file, one row at a time.
        for row_list in compound_list:
            writer.writerow(row_list)
# Call main to start this program.
if __name__ == "__main__":
    main()

#Writing a Dictionary into a CSV File
# Example 4
import csv
def main():
    heading_list = ["I-Number", "Name"]
    # Create a dictionary that contains student
    # I-Numbers and names.
    students_dict = {
        # I-Number : Name
        "751766201" : "James Smith",
        "751762102" : "Esther Einboden",
        "052058203" : "Cassidy Benavidez",
        "323021604" : "Joel Hatch",
        "251041405" : "Brianna Ririe",
        "001152306" : "Stefano Hisler",
        "182706207" : "Hyeonbeom Park",
        "124712708" : "Maren Thomas",
        "212505409" : "Tyler Clark"
    }
    # Call the write_dict function which will write
    # the students dictionary file named "students.csv".
    write_dict("students.csv", students_dict, heading_list, 0)
def write_dict(filename, dictionary, heading_list=None,
        key_column_index=None):
    """Write the contents of a dictionary into a CSV file.
    Parameters
        filename: the name of the CSV file to write
        dictionary: the dictionary to write to the CSV file
        heading_list: a list that contains the column headings.
            If heading_list is None, this function will not
            write headings to the CSV File.
        key_column_index: the index of the column in the CSV
            file where this function should write the keys.
            If key_column_index is None, this function will
            not write the keys to the CSV file.
    Return: nothing
    """
    # Open the text file for writing and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "wt", newline="") as csv_file:
        # Use the csv module to create a writer object
        # that will write to the opened CSV file.
        writer = csv.writer(csv_file)
        # Write the heading_list to the CSV file.
        if heading_list is not None:
            writer.writerow(heading_list)
        # Get each key value pair from the dictionary
        # and write each pair on a separate row in thee
        # CSV file.
        for key, value in dictionary.items():
            # If a value stored in the dictionary is a
            # list, make a temporary copy of that value.
            # Otherwise, create a list that contains the
            # value.
            if isinstance(value, list):
                row_list = value.copy()
            else:
                row_list = [value]
            # If key_column_index is an integer, insert
            # the key into the row_list so that this
            # function will write the key to the CSV file.
            if key_column_index is not None:
                row_list.insert(key_column_index, key)
            # Write a row to the CSV file.
            writer.writerow(row_list)
# Call main to start this program.
if __name__ == "__main__":
    main()