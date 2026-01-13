📚 Booklist Search & Filter Program (Python)

A menu-driven Python console application that reads book data from a text file and allows users to search, filter, and display bestseller information based on year range, rating, author, or title.

This project demonstrates file handling, list processing, user input validation, and formatted console output using Python.

📁 Project Structure
booklist.txt
book_search.py
README.md


book_search.py — Main Python program

booklist.txt — Dataset containing book information

README.md — Project documentation

📄 Dataset Format (booklist.txt)

Each line in booklist.txt represents a single book with comma-separated values:

Title,Author,Rating,Reviews,Price,Year,Genre

Example:
1984 (Signet Classics),George Orwell,4.7,21424,6,2017,Fiction

🚀 Features

The program provides the following functionality:

🔹 Search by Year Range

Enter a start year and end year

Displays all books published within that range (inclusive)

🔹 Search by Rating

Enter a specific rating (e.g., 4.7)

Displays all books that exactly match the rating

🔹 Search by Author

Enter a full or partial author name

Case-insensitive matching

🔹 Search by Title

Enter a full or partial book title

Case-insensitive matching

🔹 Clean Tabular Output

Results are displayed in aligned columns:

Title

Author

Publication Year

🧠 Program Flow

Reads all book data from booklist.txt

Stores book information in a list of lists

Displays a menu with user options

Validates all user input

Filters data based on the selected option

Displays results or a “No entries found” message

🧩 Key Functions
Function	Description
read_books()	Reads and parses book data from file
get_valid_range()	Validates year range input
get_valid_rating()	Validates rating input
print_range_data()	Displays books within a year range
print_rating_data()	Displays books matching a rating
print_author_data()	Displays books by author
print_title_data()	Displays books by title
main()	Controls menu logic and program flow
▶️ How to Run

Make sure booklist.txt is in the same directory as the Python file

Run the program:

python book_search.py


Follow the on-screen menu prompts

🛠 Technologies Used

Python 3

File I/O

Lists & loops

Exception handling

String formatting

📌 Learning Outcomes

This project demonstrates:

Reading and parsing structured data from files

Input validation and error handling

Modular programming with functions

Console-based UI design

Data filtering and searching techniques

✅ Notes

Ratings must be ≤ 5

Year range must be valid (start year < end year)

Searches are case-insensitive

Program exits cleanly using the Q option
