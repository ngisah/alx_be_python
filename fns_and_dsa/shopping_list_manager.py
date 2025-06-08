shopping_list = []
def add_item(item):
    """Add an item to the shopping list."""
    shopping_list.append(item)
    print(f"Added '{item}' to the shopping list.")
def remove_item(item):
    """Remove an item from the shopping list."""
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Removed '{item}' from the shopping list.")
    else:
        print(f"Item '{item}' not found in the shopping list.")
def view_list():
    """View the current shopping list."""
    if shopping_list:
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("The shopping list is empty.")
def exit_program():
    """Exit the shopping list manager."""
    print("Goodbye!")
    return False


def main(): 
    """Main function to run the shopping list manager."""
    print("Welcome to the Shopping List Manager!")
    running = True
    while running:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            item = input("Enter the item to add: ").strip()
            add_item(item)
        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            remove_item(item)
        elif choice == '3':
            view_list()
        elif choice == '4':
            running = exit_program()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

        