# data_tasks.py
# -----------------------------------
# Data structure tasks from Lab 3
# -----------------------------------


def get_list_element(lst, index):
    """Return an element from a list at a given index."""
    return lst[index]


def get_dict_value(dictionary, key):
    """Return a value from a dictionary using a key."""
    return dictionary.get(key, "Key not found")


def tuple_length(tpl):
    """Return the length of a tuple."""
    return len(tpl)


def unique_elements(lst):
    """Return unique elements from a list using a set."""
    return set(lst)
