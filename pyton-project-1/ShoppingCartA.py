#Author: Ashley McKinlay-Remus
print()
print("Welcome to Shopping Cart!")
print()
shopping_list = []
price_list = []
items_list = ""
shopping_list = []
total_price = 0

while items_list != "quit":
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    action = input("Please enter an action as a number: ")
    print()
    if action == "1":
        items_list = input("What item do you want to add? ")
        item_price = float(input("What is the price of the item? "))
        shopping_list.append(items_list)
        price_list.append(item_price)
        print({items_list}, "has been added to the cart")
        print()
    elif action == "2":
        print("The contents of the shopping cart are:")
        for item in items_list:
            print(item)
        #for i in range(len(items_list)):
        for i in range(len(shopping_list)):
            item = shopping_list[i]
            #price = item_price[i]
            price = price_list[i]
            print(f"{i + 1}. {item} - ${price:.2f}")
            print()
    elif action == "3":
        print("The contents of the shopping cart are:")
        for item in items_list:
            print(item)
        for i in range(len(items_list)):
            item = shopping_list[i]
            price = item_price[i]
            print(f"{i + 1}. {item} - ${price:.2f}")
            print()
            remove_item = input("What number item would you like to remove? ")
            if remove_item > len(shopping_list):
                print("Invalid number.")
            else:
                items_list.pop(remove_item - 1)
                item_price.pop(remove_item - 1)
                print("The item has been removed.")
                print()
    elif action == "4":
        for i in range(len(items_list)):
            total_price += item_price[i]
            print(f"The total price of all the items is: ${total_price:.2f}")
            print()
    elif action == "5":
        items_list = "quit"
        print("Thank you. Goodbye.")

    else:
        print("Enter a different action")
    