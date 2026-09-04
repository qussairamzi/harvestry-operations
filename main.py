import storage
import ui
import coffee_manager

def main():
    coffees = storage.load_coffees()
    while True:
        ui.show_menu()
        choice = ui.get_user_choice()

        if choice == "1":
        # View coffees  
            ui.display_coffees(coffees)
            ui.pause()

        elif choice == "2":
        # Add coffee
            coffee_manager.add_coffee(coffees)

        elif choice == "3":
        # Edit coffee
            coffee_manager.edit_coffee(coffees)
            
        elif choice == "4":
        # Delete coffee
            coffee_manager.delete_coffee(coffees)

        elif choice == "5":
        # Search coffees
            coffee_manager.search_coffees_menu(coffees)

        elif choice == "6":
        # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, 5 or 6.")


if __name__ == "__main__":
    main()