import storage
import ui
import coffee_manager
import constants

def main():
    coffees = storage.load_coffees()
    while True:
        ui.show_menu()
        choice = ui.get_user_choice()

        if choice == constants.VIEW_COFFEES:
        # View coffees  
            ui.display_coffees(coffees)
            ui.pause()

        elif choice == constants.ADD_COFFEE:
        # Add coffee
            coffee_manager.add_coffee(coffees)

        elif choice == constants.EDIT_COFFEE:
        # Edit coffee
            coffee_manager.edit_coffee(coffees)

        elif choice == constants.DELETE_COFFEE:
        # Delete coffee
            coffee_manager.delete_coffee(coffees)

        elif choice == constants.SEARCH_COFFEES:
        # Search coffees
            coffee_manager.search_coffees_menu(coffees)

        elif choice == constants.EXIT:
        # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, 5 or 6.")

if __name__ == "__main__":
    main()