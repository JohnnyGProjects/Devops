# main.py
# -----------------------------------
# Main entry point for Lab 3
# Handles user input and output
# -----------------------------------

from string_tasks import *
from data_tasks import *
from loop_tasks import *


def main():
    print("\n===== Lab 3 Interactive Program =====\n")

    # -----------------------------
    # String Tasks
    # -----------------------------
    word = input("Enter a word: ")

    print("Second character:", get_second_char(word))
    print("Reversed string:", reverse_string(word))

    step = int(input("Enter a step value for slicing: "))
    print("Sliced string:", slice_string(word, step))

    # -----------------------------
    # List Task
    # -----------------------------
    lst = list(map(int, input("\nEnter numbers for a list (space-separated): ").split()))
    index = int(input("Enter an index to retrieve: "))
    print("List element:", get_list_element(lst, index))

    # -----------------------------
    # Dictionary Task
    # -----------------------------
    dictionary = {
        "apple": 1,
        "banana": 2,
        "orange": 3
    }
    key = input("Enter a key (apple/banana/orange): ")
    print("Dictionary value:", get_dict_value(dictionary, key))

    # -----------------------------
    # Tuple Task
    # -----------------------------
    tpl = tuple(map(int, input("\nEnter numbers for a tuple (space-separated): ").split()))
    print("Tuple length:", tuple_length(tpl))

    # -----------------------------
    # Set Task
    # -----------------------------
    print("Unique elements:", unique_elements(lst))

    # -----------------------------
    # FizzBuzz Task
    # -----------------------------
    start = int(input("\nEnter FizzBuzz start number: "))
    end = int(input("Enter FizzBuzz end number: "))

    print("\nFizzBuzz Results:")
    for value in fizz_buzz(start, end):
        print(value)


# Ensures main() only runs when file is executed directly
if __name__ == "__main__":
    main()
