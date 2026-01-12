# loop_tasks.py
# -----------------------------------
# Loop-based tasks from Lab 3
# -----------------------------------


def fizz_buzz(start=1, end=100):
    """
    Print numbers from start to end.
    - Fizz for multiples of 3
    - Buzz for multiples of 5
    - FizzBuzz for both
    """
    results = []

    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            results.append("FizzBuzz")
        elif num % 3 == 0:
            results.append("Fizz")
        elif num % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(num))

    return results
