coffees = [
    {
        "name": "Mina",
        "origin": "Brazil",
        "process": "Natural",
        "roast": "Medium",
    },
    {
        "name": "Huila",
        "origin": "Colombia",
        "process": "Washed",
        "roast": "Medium",
    },

    {
        "name": "Inzuzi",
        "origin": "Rwanda",
        "process": "Natural",
        "roast": "Medium",
    },

    {
        "name": "Aquia",
        "origin": "Costa Rica",
        "process": "Natural",
        "roast": "Medium",
    },

    {
        "name": "Armonia",
        "origin": "Guatemala",
        "process": "Washed",
        "roast": "Medium",
    },
    {
        "name": "Gibuzale",
        "origin": "Uganda",
        "process": "Washed",
        "roast": "Medium",
    },
    
]

def show_menu():
    print("==============================")
    print("    HARVESTRY OPERATIONS")
    print("==============================")
    print("1. View coffees")
    print("2. Add coffee")
    print("3. Exit")

def get_user_choice():
    return input("Choose an option: ")

def main():
    while True:
        show_menu()
        choice = get_user_choice()

        if choice == "1":
            display_coffees(coffees)
            pause()

        elif choice == "2":
            new_coffee = get_new_coffee_details()
            coffees.append(new_coffee)
            print("Coffee added successfully.")
            pause()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1, 2 or 3.")

def display_coffees(coffees):
    if not coffees:
        print("No coffees available.")
        return
    for number, coffee in enumerate(coffees, start=1):
        print("\n----------------------------------------")
        print(f"Coffee {number}:")
        print(f"Name: {coffee['name']}")
        print(f"Origin: {coffee['origin']}")
        print(f"Process: {coffee['process']}")
        print(f"Roast: {coffee['roast']}")
        print("----------------------------------------")

def pause():
    input("Press Enter to return to the menu...")

def get_new_coffee_details():
    name = input("Enter coffee name: ")
    origin = input("Enter origin: ")
    process = input("Enter process: ")
    roast = input("Enter roast: ")

    return {"name": name, "origin": origin, "process": process, "roast": roast}

main()