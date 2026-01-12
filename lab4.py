# lab4.py
# Advanced version with menu system, user input, and validation


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    return max(a, b)


def animal_crackers(text):
    words = text.lower().split()
    return len(words) == 2 and words[0][0] == words[1][0]


def makes_twenty(a, b):
    return a == 20 or b == 20 or (a + b == 20)


def old_macdonald(name):
    if len(name) < 4:
        return name.capitalize()
    return name[:3].capitalize() + name[3:].capitalize()


def master_yoda(text):
    return " ".join(text.split()[::-1])


def almost_there(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10


def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


def paper_doll(text):
    return "".join(char * 3 for char in text)


def blackjack(a, b, c):
    total = a + b + c
    if total <= 21:
        return total
    if 11 in (a, b, c):
        total -= 10
    return total if total <= 21 else "BUST"


def summer_69(arr):
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


# -------------------------
# Helper Functions
# -------------------------
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a valid integer.")


def get_int_list(prompt):
    while True:
        try:
            return list(map(int, input(prompt).split()))
        except ValueError:
            print("❌ Enter numbers separated by spaces.")


# -------------------------
# Menu System
# -------------------------
def display_menu():
    print("\n====== Lab 4 Menu ======")
    print("1. Lesser of Two Evens")
    print("2. Animal Crackers")
    print("3. Makes Twenty")
    print("4. Old MacDonald")
    print("5. Master Yoda")
    print("6. Almost There")
    print("7. Has 33")
    print("8. Paper Doll")
    print("9. Blackjack")
    print("10. Summer of '69")
    print("0. Exit")


def main():
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


if __name__ == "__main__":
    main()
