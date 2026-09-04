import ui
import storage

def search_coffees_menu(coffees):
    search_term = ui.get_non_empty_input("Enter search term: ")
    results = search_coffees(coffees, search_term)

    if results:
        print(f"\nFound {len(results)} result(s):")
        ui.display_coffees(results)
    else:
        print("No coffees found matching the search term.")

    ui.pause()

def add_coffee(coffees):
            new_coffee = get_new_coffee_details(coffees)
            coffees.append(new_coffee)
            storage.save_coffees(coffees)
            print("Coffee added successfully.")
            pause()

def delete_coffee(coffees):
    search_name = ui.get_non_empty_input("Enter the name of the coffee to delete: ")
    coffee = find_coffee_by_name(coffees, search_name)

    if coffee:
        confirm = input(f"Are you sure you want to delete {coffee['name']}? (y/n): ").strip().lower()
        if confirm == "y":
            coffees.remove(coffee)
            storage.save_coffees(coffees)
            print("Coffee deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print("Coffee not found.")

    ui.pause()

def edit_coffee(coffees):
    search_name = ui.get_non_empty_input("Enter the name of the coffee to edit: ")
    coffee = find_coffee_by_name(coffees, search_name)

    if coffee:
        edit_coffee_details(coffee)
        storage.save_coffees(coffees)
        print("Coffee updated successfully.")
    else:
        print("Coffee not found.")

    ui.pause()

def get_new_coffee_details(coffees):
    while True:
        name = ui.get_non_empty_input("Enter coffee name: ")
        if not find_coffee_by_name(coffees, name):
            break

        print("A coffee with this name already exists. Please enter a different name.")

    origin = ui.get_non_empty_input("Enter origin: ")
    process = ui.get_non_empty_input("Enter process: ")
    roast = ui.get_non_empty_input("Enter roast: ")

    return {"name": name, "origin": origin, "process": process, "roast": roast}

def find_coffee_by_name(coffees, name):
    for coffee in coffees:
        if coffee["name"].lower() == name.lower():
            return coffee
    return None

def edit_coffee_details(coffee):
    print("Leave a field blank to keep the current value.")
    new_name = input(f"Enter new name (current: {coffee['name']}): ").strip()
    new_origin = input(f"Enter new origin (current: {coffee['origin']}): ").strip()
    new_process = input(f"Enter new process (current: {coffee['process']}): ").strip()
    new_roast = input(f"Enter new roast (current: {coffee['roast']}): ").strip()

    if new_name:
        coffee["name"] = new_name
    if new_origin:
        coffee["origin"] = new_origin
    if new_process:
        coffee["process"] = new_process
    if new_roast:
        coffee["roast"] = new_roast

def search_coffees(coffees, search_term):
    search_term = search_term.lower()
    results = []
    for coffee in coffees:
        if (search_term in coffee["name"].lower() or
            search_term in coffee["origin"].lower() or
            search_term in coffee["process"].lower() or
            search_term in coffee["roast"].lower()):
            results.append(coffee)
    return results