# tasks.py
# -----------------------------------
# This file contains all core task functions.
# Each function performs a single operation and
# does NOT handle user input or printing.
# -----------------------------------


def lesser_of_two_evens(a, b):
    """Return the lesser of two numbers if both are even,
    otherwise return the greater."""
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    return max(a, b)


def animal_crackers(text):
    """Return True if both words start with the same letter."""
    words = text.lower().split()
    return len(words) == 2 and words[0][0] == words[1][0]


def makes_twenty(a, b):
    """Return True if either number is 20 or their sum is 20."""
    return a == 20 or b == 20 or (a + b == 20)


def old_macdonald(name):
    """Capitalize the first and fourth letters of a name."""
    if len(name) < 4:
        return name.capitalize()
    return name[:3].capitalize() + name[3:].capitalize()


def master_yoda(text):
    """Reverse the order of words in a sentence."""
    return " ".join(text.split()[::-1])


def almost_there(n):
    """Return True if n is within 10 of 100 or 200."""
    return abs(100 - n) <= 10 or abs(200 - n) <= 10


def has_33(nums):
    """Return True if the list contains two consecutive 3s."""
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


def paper_doll(text):
    """Return a string where each character is repeated 3 times."""
    return "".join(char * 3 for char in text)


def blackjack(a, b, c):
    """Return the sum of three numbers following blackjack rules."""
    total = a + b + c

    # If total is already valid, return it
    if total <= 21:
        return total

    # Adjust for an ace (11) if present
    if 11 in (a, b, c):
        total -= 10

    # Final check for bust
    return total if total <= 21 else "BUST"


def summer_69(arr):
    """Return the sum of numbers, ignoring values between 6 and 9 inclusive."""
    total = 0
    skip = False

    for num in arr:
        if num == 6:
            skip = True
        elif num == 9 and skip:
            skip = False
        elif not skip:
            total += num

    return total
