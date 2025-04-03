import csv
def read_dictionary(products, product):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
    filename: the name of the CSV file to read.
    key_column_index: the index of the column
    to use as the keys in the dictionary.
    Return: a compound dictionary that contains
    the contents of the CSV file.
    """
    dictionary = {}
    with open("products.csv", "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            key = row_list[product]
            dictionary[key] = row_list
    return dictionary
def main():
    product = 0
    dictionary = read_dictionary("products.csv", product)
    print("All Products")
    print(dictionary) 
    print("Requested Items")
    #for key, value in dictionary.items():
        #print(f"{key}: {value}")
    with open("request.csv", "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            #row_list[0] = "ok"
            if row_list[0] in dictionary:
                print(f"{dictionary[row_list[0]][1]}: {row_list[1]} @ {dictionary[row_list[0]][2]}")
                #row_list.append(dictionary[row_list[0]])
            else:
                row_list.append("Not Found")
            #print(row_list)
        
    
    
if __name__ == "__main__":
    main()
    