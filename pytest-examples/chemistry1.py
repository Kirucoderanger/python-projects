def make_periodic_table():
    """
    Create and return a compound list containing data for all 94 naturally occurring elements.
    Each element is represented as a dictionary with keys: 'symbol', 'name', and 'atomic_number'.
    """
    periodic_table = [
        {"symbol": "H", "name": "Hydrogen", "atomic_number": 1},
        {"symbol": "He", "name": "Helium", "atomic_number": 2},
        {"symbol": "Li", "name": "Lithium", "atomic_number": 3},
        {"symbol": "Be", "name": "Beryllium", "atomic_number": 4},
        {"symbol": "B", "name": "Boron", "atomic_number": 5},
        {"symbol": "C", "name": "Carbon", "atomic_number": 6},
        {"symbol": "N", "name": "Nitrogen", "atomic_number": 7},
        {"symbol": "O", "name": "Oxygen", "atomic_number": 8},
        {"symbol": "F", "name": "Fluorine", "atomic_number": 9},
        {"symbol": "Ne", "name": "Neon", "atomic_number": 10},
        # Add remaining elements up to atomic number 94
        {"symbol": "Pu", "name": "Plutonium", "atomic_number": 94},
    ]
    return periodic_table
periodic_table_list = [
    # [symbol, name, atomic_mass]
    ["Ac", "Actinium", 227],
    ["Ag", "Silver", 107.8682],
    ["Al", "Aluminum", 26.9815386],
      
]

def main():
    periodic_table = make_periodic_table()
    for element in periodic_table:
        print(f"Symbol: {element['symbol']}, Name: {element['name']}, Atomic Number: {element['atomic_number']}")

        def get_user_input():
            chemical_formula = input("Enter the chemical formula for the molecule: ")
            sample_mass = float(input("Enter the mass of the chemical sample in grams: "))
            return chemical_formula, sample_mass

        def print_element_details(periodic_table_list):
            for element in periodic_table_list:
                print(f"Name: {element[1]}, Atomic Mass: {element[2]}")

        chemical_formula, sample_mass = get_user_input()
        print_element_details(periodic_table_list)


periodic_table_list = [
    # [symbol, name, atomic_mass]
    ["Ac", "Actinium", 227],
    ["Ag", "Silver", 107.8682],
    ["Al", "Aluminum", 26.9815386],]


if __name__ == "__main__":
    main()