import random
import csv
# Sample dictionary
products = {
    "A101": ("Wireless Mouse", 25.00),
    "D083": ("Bluetooth Speaker", 40.00),
    "B205": ("Laptop Stand", 30.00),
    "C300": ("Webcam", 50.00)
}

# Randomly select a key
random_key = random.choice(list(products.keys()))

# Access value using that key
description, price = products[random_key]

# Display
print("🎯 RANDOM PRODUCT SELECTED")
print(f"Code:        {random_key}")
print(f"Description: {description}")
print(f"Price:       ${price:.2f}")



def request_random():
    request = {}
    with open("request.csv", mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        next(reader)
        for row_list in reader:
            request[row_list['id']] = row_list
    random_key = random.choices(list(request.keys()))
    print(random_key)
    print(request[random_key])
        
            
           
    
def display_random():
    dictionary = request_random()
    random_key = random.choices(list(dictionary.keys()))
    print(random_key)
    
import csv
import random

# Step 1: Read the CSV file and form a dictionary
"""my_dict = {}
with open('request.csv', mode='r') as file:
    reader = csv.DictReader(file)
    next(reader)
    for row_list in reader:
        key = row_list[0][0]  # Assuming 'product' is the key column
        my_dict[key] = row_list
    headers = reader.fieldnames  # Get the headers from the CSV file
    print(f"Headers: {headers}")
    #for row in reader:
        #print(f"Row: {row}")
        #row = {key.strip(): value.strip() for key, value in row.items()}
        #my_dict[row['product']] = row  # Use 'id' as the key and store the rest of the row as the value

# Step 2: Randomly select a key
random_key = random.choice(list(my_dict.keys()))
print(f"Random Key: {random_key}")

# Step 3: Randomly select a value (whole row)
random_value = my_dict[random_key]
print(f"Random Value (Row): {random_value}")

# Step 4: Randomly select a key-value pair
random_pair = random.choice(list(my_dict.items()))
print(f"Random Key-Value Pair: {random_pair}")"""
product = 0
my_dict = {}
with open('request.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row_list in reader:
        key = row_list[product]  # Assuming 'product' is the key column
        my_dict[key] = row_list
    #headers = reader.fieldnames  # Get the headers from the CSV file
    #print(f"Headers: {headers}")
    for row in reader:
        print(f"Row: {row}")
        row = {key.strip(): value.strip() for key, value in row.items()}
        my_dict[row[product]] = row  # Use 'id' as the key and store the rest of the row as the value
    random_key = random.choice(list(my_dict.keys()))
    print(f"Random Key: {random_key}")    


