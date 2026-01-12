# main.py
# -----------------------------------
# Main entry point for the program.
# Handles user interaction and calls
# task functions.
# -----------------------------------

from tasks import *
from utils import get_int, get_int_list
from menu import display_menu


def main():
    """Main program loop."""
    while True:
        display_menu()
        choice = get_int("Select an option: ")

        if choice == 0:
            print("👋 Exiting program. Goodbye!")
            break

        elif choice == 1:
            a = get_int("Enter first number: ")
            b = get_int("Enter second number: ")
            print("Result:", lesser_of_two_evens(a, b))

        elif choice == 2:
            text = input("Enter two words: ")
            print("Result:", animal_crackers(text))

        elif choice == 3:
            a = get_int("Enter first number: ")
            b = get_int("Enter second number: ")
            print("Result:", makes_twenty(a, b))

        elif choice == 4:
            name = input("Enter a name: ")
            print("Result:", old_macdonald(name))

        elif choice == 5:
            text = input("Enter a sentence: ")
            print("Result:", master_yoda(text))

        elif choice == 6:
            n = get_int("Enter a number: ")
            print("Result:", almost_there(n))

        elif choice == 7:
            nums = get_int_list("Enter numbers separated by spaces: ")
            print("Result:", has_33(nums))

        elif choice == 8:
            text = input("Enter text: ")
            print("Result:", paper_doll(text))

        elif choice == 9:
            a = get_int("Enter first card: ")
            b = get_int("Enter second card: ")
            c = get_int("Enter third card: ")
            print("Result:", blackjack(a, b, c))

        elif choice == 10:
            nums = get_int_list("Enter numbers separated by spaces: ")
            print("Result:", summer_69(nums))

        else:
            print("❌ Invalid menu option.")


# Ensures main() only runs when this file is executed directly
if __name__ == "__main__":
    main()
