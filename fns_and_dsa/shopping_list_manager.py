def display_menu():
    """Display the main menu options."""
    print("\n" + "="*30)
    print("Shopping List Manager")
    print("="*30)
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("="*30)

def main():
    """Main function to run the shopping list manager."""
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            # Add item
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' added to shopping list.")
            else:
                print("Item cannot be empty.")
                
        elif choice == '2':
            # Remove item
            if not shopping_list:
                print("Shopping list is empty.")
                continue
                
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from shopping list.")
            else:
                print(f"'{item}' not found in shopping list.")
                
        elif choice == '3':
            # View list
            if not shopping_list:
                print("Shopping list is empty.")
            else:
                print("\nCurrent Shopping List:")
                print("-" * 20)
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                    
        elif choice == '4':
            # Exit
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()