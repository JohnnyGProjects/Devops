# string_tasks.py
# -----------------------------------
# String-related tasks from Lab 3
# -----------------------------------


def get_second_char(word):
    """Return the second character of a string."""
    return word[1]


def reverse_string(word):
    """Return the reversed version of a string."""
    return word[::-1]


def slice_string(word, step=2):
    """Return a sliced version of a string using a step."""
    return word[::step]
