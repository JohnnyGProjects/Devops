def main():
    bestsellers_list = read_data()
    inp = 0
    while True:
        print(
            '\n1 Enter your year range \n2 Enter minimum Rating \n3 Search for author \n4 Search for title \nQ Quit \n')
        inp = input("Enter your choice > ").lower()
        if inp == '1':
            beginning_year = int(input('Enter start year: '))
            ending_year = int(input('Enter ending year: '))
            search_by_years(beginning_year, ending_year, bestsellers_list)
        elif inp == '2':
            rating = float(input('Enter rating : '))
            search_by_rating(rating, bestsellers_list)
        elif inp == '3':
            auth_search_str = input('Enter an author\'s name (or part of a name): ').capitalize()
            search_by_author(auth_search_str, bestsellers_list)
        elif inp == '4':
            title_search_str = input('Enter a title (or part of a title): ').capitalize()
            search_by_title(title_search_str, bestsellers_list)
        elif inp == 'q':
            print("Goodbye")
            break
        else:
            print("invalid input,try again!")

def read_data():
    """
    The program will input the data set and construct a list of books. If the list of books cannot be constructed, the program will display an appropriate error message and halt.
    """
    inp_name = []
    with open('booklist.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().split(",")
            inp_name.append(line)

    return inp_name


def search_by_years(beginning_year, ending_year, bestsellers_list):
    """
    Prompt the user for two years (a starting year and an ending year), then display all books between those two years (inclusive).
    For example, if the user entered “2016” and “2019”, display all books published in 2016, 2017, 2018, and 2019.
    """
    print('{:65s} |{:35s}|{:6s} '.format("Title", "Author", "Publication Date"))
    print("-" * (119))
    not_found = True
    year_range = range(beginning_year, ending_year + 1, 1)
    for title, author, rating, reviews, price, date, genre in bestsellers_list:
        for year in year_range:
            if str(year) in date:
                print('{:65s} |{:35s}|{:6s} '.format(title.strip()[:55], author.strip(), date))
                not_found = False
    if (not_found):
        print("No Entries Found")


def search_by_rating(ratng, bestsellers_list):
    """
    Prompt the user to enter a rating, then displayall books with a rating equal to the entered rating.
    For example, if the user entered 4.7,display all books with a rating equal to 4.7.
    """
    print('{:65s} |{:35s}|{:6s} '.format("Title", "Author", "Publication Date"))
    print("-" * (119))
    not_found = True
    for title, author, rating, reviews, price, date, genre in bestsellers_list:
        if float(rating) == ratng:
            print('{:65s} |{:35s}|{:6s} '.format(title.strip()[:55], author.strip(), date))
            not_found = False
    if (not_found):
        print("No Entries Found")
def search_by_author(str, bestsellers_list):
    """
    Prompt the user for a string, then display all books whose author’s name contains that string (regardless of case).
    For example, if the user enters “ST”, display all books whose author’s name contains (or matches) the string “ST”, “St”, “sT” or “st”.
    """
    print('{:65s} |{:35s}|{:6s} '.format("Title", "Author", "Publication Date"))
    print("-" * (119))
    not_found = True
    for title, author, rating, reviews, price, date, genre in bestsellers_list:
        if str in author:
            print('{:65s} |{:35s}|{:6s} '.format(title.strip()[:55], author.strip(), date))
            not_found = False
    if (not_found):
        print("No Entries Found")

def search_by_title(title_search_str, bestsellers_list):
    """
    Prompt the user for a string, then display all books whose title contains that string (regardless of case).
    For example, if the user enters “secret”, three books are found: “The Secret of Santa Vittoria” by Robert Crichton, “The Secret Pilgrim” by John le Carré, and “Harry Potter and the Chamber of Secrets”.
    Harry Potter and the Chamber of Secrets, by J. K. Rowling
    The Secret of Santa Vittoria, by Robert Crichton
    The Secret Pilgrim, by John le Carre
    """
    print('{:65s} |{:35s}|{:6s} '.format("Title", "Author", "Publication Date"))
    print("-" * (119))
    not_found = True
    for title, author, rating, reviews, price, date, genre in bestsellers_list:
        if title_search_str in title:
            print('{:65s} |{:35s}|{:6s} '.format(title.strip()[0:55], author.strip(), date))
            not_found = False
    if (not_found):
        print("No Entries Found")

if __name__ == "__main__":
    main()