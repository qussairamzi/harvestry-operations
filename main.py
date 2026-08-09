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
    show_menu()
    choice = get_user_choice()
    print(f"You chose: {choice}")


main()