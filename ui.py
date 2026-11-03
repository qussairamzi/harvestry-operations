import constants

def show_menu():
    print("==============================")
    print("    HARVESTRY OPERATIONS")
    print("==============================")
    print(f"{constants.VIEW_COFFEES}. View coffees")
    print(f"{constants.ADD_COFFEE}. Add coffee")
    print(f"{constants.EDIT_COFFEE}. Edit coffee")
    print(f"{constants.DELETE_COFFEE}. Delete coffee")
    print(f"{constants.SEARCH_COFFEES}. Search coffees")
    print(f"{constants.EXIT}. Exit")

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

def get_yes_no_input(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ["y", "yes"]:
            return "y"
        elif value in ["n", "no"]:
            return "n"
        print("Invalid input. Please enter 'y', 'yes', 'n' or 'no'.")