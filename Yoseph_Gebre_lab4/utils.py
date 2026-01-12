# utils.py
# -----------------------------------
# Utility functions for user input
# and validation.
# -----------------------------------


def get_int(prompt):
    """Safely prompt the user for an integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a valid integer.")


def get_int_list(prompt):
    """Prompt the user for a list of integers separated by spaces."""
    while True:
        try:
            return list(map(int, input(prompt).split()))
        except ValueError:
            print("❌ Enter numbers separated by spaces.")
