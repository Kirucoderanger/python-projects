import csv
from datetime import datetime
import datetime
import random
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
    request = 0
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
            try:
                # Print store name
                print("\nWelcome to Grocery Store!\n")

                # Initialize variables
                total_items = 0
                subtotal = 0.0
                sales_tax_rate = 0.06

                # Print ordered items and calculate totals
                print("Ordered Items:")
                with open("request.csv", "rt") as csv_file:
                    reader = csv.reader(csv_file)
                    next(reader)
                    for row_list in reader:
                        if row_list[0] in dictionary:
                            product_name = dictionary[row_list[0]][1]
                            quantity = int(row_list[1])
                            price = float(dictionary[row_list[0]][2])
                            total_price = quantity * price
                            print(f"{product_name}: {quantity} @ ${price:.2f} = ${total_price:.2f}")
                            total_items += quantity
                            subtotal += total_price
                        else:
                            print(f"Item with ID {row_list[0]}: Not Found")

                # Calculate totals
                sales_tax = subtotal * sales_tax_rate
                total_due = subtotal + sales_tax

                # Print totals
                print("\nSummary:")
                print(f"Number of Items: {total_items}")
                print(f"Subtotal: ${subtotal:.2f}")
                print(f"Sales Tax (6%): ${sales_tax:.2f}")
                print(f"Total Due: ${total_due:.2f}")

                # Print thank you message
                print("\nThank you for shopping with us!")

                # Print current date and time
                current_time = datetime.datetime.now()
                print(f"\nDate and Time: {current_time:%Y-%m-%d %H:%M:%S}")
                
                
                print("\n--- Additional Info ---")
                print(f"🕒 Return by: {return_by_date()}")
                print(f"🎉 {days_until_new_year()} days left until the New Year's Sale!")
                print(get_random_product("request.csv" ))
                    
                print("Thank you for shopping with us!")
                print("Have a great day!")
                print("Goodbye!")

            except FileNotFoundError as e:
                print(f"Error: {e}. Please ensure the file exists.")
            except PermissionError as e:
                print(f"Error: {e}. Please check your file permissions.")
            except KeyError as e:
                print(f"Error: Missing key {e} in the dictionary.")
                
def days_until_new_year():
    today = datetime.date.today()
    new_year = datetime.date(today.year + 1, 1, 1)
    return (new_year - today).days

def return_by_date():
    return_date = datetime.datetime.now() + datetime.timedelta(days=30)
    return return_date.replace(hour=21, minute=0, second=0, microsecond=0).strftime('%Y-%m-%d %I:%M %p')


def get_random_product(csv_file):
    product = 0
    my_dict = {}
    with open('request.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row_list in reader:
            key = row_list[product]  # Assuming 'product' is the key column
            my_dict[key] = row_list
    
        for row in reader:
            print(f"Row: {row}")
            row = {key.strip(): value.strip() for key, value in row.items()}
            my_dict[row[product]] = row  # Use 'id' as the key and store the rest of the row as the value
        random_key = random.choice(list(my_dict.keys()))
        print(f"Random Key: {random_key}")
        return f"💸 COUPON: 15% OFF your next {random_key.upper()}!"
    

    
import datetime
import random

# Sample shopping cart: item_code -> (description, quantity, price)
cart = {
    "A101": ("Wireless Mouse", 1, 25.00),
    "D083": ("Bluetooth Speaker", 3, 40.00),
    "B205": ("Laptop Stand", 1, 30.00)
}

def apply_discount(cart):
    total = 0
    receipt_lines = []
    for code, (desc, qty, price) in cart.items():
        if code == "D083":
            full_price_qty = qty // 2 + qty % 2
            half_price_qty = qty // 2
            full_price_total = full_price_qty * price
            half_price_total = half_price_qty * (price / 2)
            item_total = full_price_total + half_price_total
            receipt_lines.append(f"{desc} x{qty} - ${item_total:.2f} (includes {half_price_qty} @ 50% off)")
            total += item_total
        else:
            item_total = qty * price
            receipt_lines.append(f"{desc} x{qty} - ${item_total:.2f}")
            total += item_total
    return receipt_lines, total

def days_until_new_year():
    today = datetime.date.today()
    new_year = datetime.date(today.year + 1, 1, 1)
    return (new_year - today).days

def return_by_date():
    return_date = datetime.datetime.now() + datetime.timedelta(days=30)
    return return_date.replace(hour=21, minute=0, second=0, microsecond=0).strftime('%Y-%m-%d %I:%M %p')

def generate_coupon(cart):
    product = random.choice(list(cart.values()))
    return f"🎟️ COUPON: 15% OFF your next {product[0]} purchase!"

# Generate receipt
lines, total_price = apply_discount(cart)

print("====== RECEIPT ======")
for line in lines:
    print(line)
print(f"TOTAL: ${total_price:.2f}")

print("\n--- Additional Info ---")
print(f"🕒 Return by: {return_by_date()}")
print(f"🎉 {days_until_new_year()} days left until the New Year's Sale!")
print(generate_coupon(cart))
print("======================")




                
        
    
    
if __name__ == "__main__":
    main()
    