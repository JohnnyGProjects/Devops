🧪 Lab 4 – Python Functions & Menu-Driven Program

This project is a menu-driven Python console application that allows users to interactively run a collection of small programming tasks.
Each task is implemented as a standalone function, while user input, validation, and menu display are handled in separate modules.

The project emphasizes modular design, function logic, and clean separation of concerns.

📁 Project Structure
main.py
menu.py
tasks.py
utils.py
README.md

File Overview

main.py – Program entry point; handles user interaction and controls program flow

menu.py – Displays the interactive menu options

tasks.py – Contains all core task functions (no input/output logic)

utils.py – Utility functions for safe user input and validation

🚀 Program Features

Users can select from multiple programming challenges via an interactive menu:

🔢 Numerical Logic

Lesser of Two Evens – Returns the smaller number if both are even, otherwise the larger

Makes Twenty – Checks if either number is 20 or their sum is 20

Almost There – Checks if a number is within 10 of 100 or 200

Blackjack – Calculates card totals using blackjack rules

Summer of ’69 – Sums numbers while ignoring values between 6 and 9 (inclusive)

🔤 String Manipulation

Animal Crackers – Checks if two words start with the same letter

Old MacDonald – Capitalizes the first and fourth letters of a name

Master Yoda – Reverses the word order in a sentence

Paper Doll – Repeats each character in a string three times

📋 List Processing

Has 33 – Checks if a list contains two consecutive 3s

🧠 Core Functions (tasks.py)
Function	Description
lesser_of_two_evens()	Returns the lesser of two even numbers
animal_crackers()	Checks matching starting letters
makes_twenty()	Validates if 20 is involved
old_macdonald()	Capitalizes name letters
master_yoda()	Reverses sentence word order
almost_there()	Checks proximity to 100 or 200
has_33()	Detects consecutive 3s
paper_doll()	Repeats characters
blackjack()	Applies blackjack scoring logic
summer_69()	Sums values while skipping a range
🧭 Program Flow

Menu is displayed using display_menu()

User selects an option

Input is safely validated via utils.py

Corresponding function from tasks.py is executed

Result is displayed

Program loops until the user selects Exit

▶️ How to Run

Ensure all files are in the same directory

Run the program:

python main.py


Follow the on-screen menu prompts

🛠 Technologies Used

Python 3

Modular programming

Functions and conditionals

Loops and list processing

Input validation with exception handling

📌 Learning Outcomes

This project demonstrates:

Clean separation of logic, input, and UI

Reusable and testable functions

Menu-driven program design

Defensive programming with input validation

Readable and maintainable Python code

✅ Notes

Program exits cleanly using menu option 0

All user input is validated to prevent crashes

Designed for educational and learning purposes
