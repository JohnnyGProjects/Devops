

def read_books():
    f = open("booklist.txt",encoding="UTF-8")
    list = []
    for book in f:
        lst = []
        book = book.rstrip()
        data = book.split(",")
        lst.append(data[0])
        lst.append(data[1])
        lst.append(float(data[2]))
        lst.append(int(data[3]))
        lst.append(int(data[4]))
        lst.append(int(data[5]))
        lst.append(data[6])
        list.append(lst)
    return list
def get_valid_range():
    while True:
        try:
            start_year = int(input("Enter start year "))
            end_year = int(input(" Enter end year "))
            if end_year > start_year:
                return start_year,end_year
            else:
                print("\nstart year must be before end year")
                continue
        except:
            print("invalid input,try again!")
            continue



def print_rating_data(data,compare_rating):
    books = []
    for d in data:
        rating = d[2]
        if    rating == compare_rating:
            books.append(d)
    if len(books) > 0:
        aligned_string = "{:<111}|{:<32}|{:<10}".format("Title", "Author", "Publication Date")
        print(aligned_string)
        print("*"*(111+32+10))
        for b in books:
            aligned_string = "{:<111}|{:<32}|{:<10}".format(b[0].strip(),b[1].strip(),b[-2])
            print(aligned_string)
    else:
        print("No entries found.")
def print_range_data(data,start_year,end_year):
    books = []
    for d in data:
        year = d[-2]
        if    start_year <= year <= end_year:
            books.append(d)
    if len(books) > 0:
        aligned_string = "{:<111}|{:<32}|{:<10}".format("Title", "Author", "Publication Date")
        print(aligned_string)
        print("*"*(111+32+10))
        for b in books:
            aligned_string = "{:<111}|{:<32}|{:<10}".format(b[0].strip(),b[1].strip(),b[-2])
            print(aligned_string)
    else:
        print("No entries found.")


def print_author_data(data,user_author):
    books = []
    user_author = user_author.lower()
    for d in data:
        author = d[1].lower()
        if    user_author in author:
            books.append(d)
    if len(books) > 0:
        aligned_string = "{:<111}|{:<32}|{:<10}".format("Title", "Author", "Publication Date")
        print(aligned_string)
        print("*"*(111+32+10))
        for b in books:
            aligned_string = "{:<111}|{:<32}|{:<10}".format(b[0].strip(),b[1].strip(),b[-2])
            print(aligned_string)
    else:
        print("No entries found.")
def print_title_data(data,user_title):
    books = []
    user_title = user_title.lower()
    for d in data:
        title = d[0].lower()
        if    user_title in title:
            books.append(d)
    if len(books) > 0:
        aligned_string = "{:<111}|{:<32}|{:<10}".format("Title", "Author", "Publication Date")
        print(aligned_string)
        print("*"*(111+32+10))
        for b in books:
            aligned_string = "{:<111}|{:<32}|{:<10}".format(b[0].strip(),b[1].strip(),b[-2])
            print(aligned_string)
    else:
        print("No entries found.")

def get_valid_rating():
    while True:
        try:
            rating = float(input("Enter rating : "))
            if rating > 5:
                print("Invalid rating,rating ,must be maximum 5")
                continue
            return rating
        except:
            print("invalid input,try again!")


def main():
    books_data = read_books()
    while True:
        print("1 Enter year range")
        print("2 Enter minimum rating")
        print("3 Search for author")
        print("4 Search for title")
        print("Q Quit")
        ch = input("Enter your choice > ")
        if ch == '1':
            start_year,end_year = get_valid_range()
            print_range_data(books_data,start_year,end_year)
        elif ch == '2':
            rating = get_valid_rating()
            print_rating_data(books_data,rating)
        elif ch == '3':
            author = input("Enter an author’s name (or part of a name): ")
            print_author_data(books_data,author)
        elif ch == '4':
            title = input("Enter a title (or part of a title):")
            print_title_data(books_data,title)
        elif ch.lower() == 'q':
            print("Good Bye")
            break
        else:
            print("invalid input,try again!")


read_books()
if __name__ == '__main__':
    main()