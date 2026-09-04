def show_menu():
    print("==============================")
    print("    HARVESTRY OPERATIONS")
    print("==============================")
    print("1. View coffees")
    print("2. Add coffee")
    print("3. Edit coffee")
    print("4. Delete coffee")
    print("5. Search coffees")
    print("6. Exit")

def get_user_choice():
    return get_non_empty_input("Choose an option: ")

def display_coffees(coffees):
    if not coffees:
        print("No coffees available.")
        return
    sorted_coffees = sorted(coffees, key=lambda coffee: coffee["name"].lower())
    for number, coffee in enumerate(sorted_coffees, start=1):
        print("\n----------------------------------------")
        print(f"Coffee {number}:")
        print(f"Name: {coffee['name']}")
        print(f"Origin: {coffee['origin']}")
        print(f"Process: {coffee['process']}")
        print(f"Roast: {coffee['roast']}")
        print("----------------------------------------")

def pause():
    input("Press Enter to return to the menu...")

def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")