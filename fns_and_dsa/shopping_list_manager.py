#!/usr/bin/env python3
"""
shopping_list_manager.py

A simple command-line application for managing a shopping list 
using Python lists.
"""

def display_menu():
    """Displays the main menu options to the user."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """The main function to run the shopping list manager."""
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Add Item
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty.")
                
        elif choice == '2':
            # Remove Item
            if not shopping_list:
                print("The shopping list is empty. Nothing to remove.")
                continue

            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove in shopping_list:
                try:
                    shopping_list.remove(item_to_remove)
                    print(f"'{item_to_remove}' removed from the list.")
                except ValueError:
                    # Should not happen if 'if item_to_remove in shopping_list' is correct, 
                    # but kept for robust practice.
                    print(f"Error removing '{item_to_remove}'.")
            else:
                print(f"'{item_to_remove}' not found in the list.")
                
        elif choice == '3':
            # View List
            print("\n--- Current Shopping List ---")
            if shopping_list:
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            else:
                print("The shopping list is empty.")
            print("---------------------------")
            
        elif choice == '4':
            # Exit
            print("Goodbye!")
            break
            
        else:
            # Invalid choice
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()