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


main()