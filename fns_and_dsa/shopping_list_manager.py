def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            new_item = input("Enter the item to add: ")
            shopping_list.append(new_item)
            print(new_item, "has been added to your shopping list.")
            print("Here is your updated shopping list: ", shopping_list)

        elif choice == "2":
            print(shopping_list)
            remove_item = input("Enter the item you want to remove: ")
            shopping_list.remove(remove_item)
            print(remove_item, "has been removed from your shopping list.")

        elif choice == "3":
            print("Here is your shopping list: ", shopping_list)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()