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
    print("3. Edit coffee")
    print("4. Delete coffee")
    print("5. Exit")

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
            search_name = input("Enter the name of the coffee to edit: ")
            coffee = find_coffee_by_name(coffees, search_name)
            if coffee:
                edit_coffee_details(coffee)
                print("Coffee updated successfully.")
            else:
                print("Coffee not found.")
            pause()

        elif choice == "4":
            search_name = input("Enter the name of the coffee to delete: ")
            coffee = find_coffee_by_name(coffees, search_name)
            if coffee:
                confirm = input(f"Are you sure you want to delete '{coffee['name']}'? (y/n): ").strip().lower()
                if confirm == "y":
                    coffees.remove(coffee)
                    print("Coffee deleted successfully.")
                else:
                    print("Deletion cancelled.")
            else:
                print("Coffee not found.")
            pause()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, 4 or 5.")

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

def find_coffee_by_name(coffees, name):
    for coffee in coffees:
        if coffee["name"].lower() == name.lower():
            return coffee
    return None

def edit_coffee_details(coffee):
    print("Leave a field blank to keep the current value.")
    new_name = input(f"Enter new name (current: {coffee['name']}): ")
    new_origin = input(f"Enter new origin (current: {coffee['origin']}): ")
    new_process = input(f"Enter new process (current: {coffee['process']}): ")
    new_roast = input(f"Enter new roast (current: {coffee['roast']}): ")

    if new_name:
        coffee["name"] = new_name
    if new_origin:
        coffee["origin"] = new_origin
    if new_process:
        coffee["process"] = new_process
    if new_roast:
        coffee["roast"] = new_roast

main()