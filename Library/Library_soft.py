class Book:
    def __init__(self, title, author, genre, availability):
        self.title = title
        self.author = author
        self.genre = genre
        self.availability = availability

    def __str__(self):
        return f'{self.title} by {self.author} |{self.genre}|-{"Available" if self.availability else "Unavailable"}'


class Patron:

    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id


class Library:
    def __init__(self):
        self.all_books = []
        self.patrons = []
        self.books_available = []

    def add_book(self, title, author, genre, availability):
        title = Book(title, author, genre, availability)
        self.all_books.append(title)
        if title.availability:
            self.books_available.append(title)

    def register_patron(self, name, patron_id):
        patron_id = Patron(name, patron_id)
        self.patrons.append(patron_id)
        return patron_id


class Search:
    class Search:
    def search_for_available(self):
        available_books = [book for book in lib.books_available]
        return available_books


    def search_for_book(self):
        ...

lib = Library()
class Methods:
    def check_out(self, book_):
        for object in books:
            if object.title == book_:
                object.availability = False
                if object in books_available:
                    lib.books_available.remove(object)
                    # if object not in Library.books_unavailable:

    def return_book(self, book_):
        for object in books:
            if object.title == book_:
                object.availability = True
                if object not in books_available:
                    lib.books_available.append(object)


filters = Search()

cd = Methods()
lib.add_book('HarryPotter', 'Jonh Crhis', 'fantasy', True)
lib.add_book('Rich dad poor dad', 'Sakato Nakamura', 'Business', False)
lib.add_book('The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', True)
lib.add_book('To Kill a Mockingbird', 'Harper Lee', 'Classics', True)
lib.add_book('1984', 'George Orwell', 'Dystopian', False)
lib.add_book('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', False)

lib.register_patron('Sam', 188)
lib.register_patron('Nick', 127)
lib.register_patron('Mike', 257)

books = lib.all_books
patronslist = lib.patrons
books_available = lib.books_available


def display_commands():
    print('commands: \nshow (|view all books|)\npatrons (|view all patrons|)')
    print('instock(|show all available|)\noutstock(|show all unavailable|)')
    print('add (|add a book|)\nregister(|register a patron|)\nget (|check out a book|)')
    print('return (|return a book|)')
    command = input('command: ')
    print()
    return command



def main():
    print('Wellcome to the library!  ')
    # print("Register to continue")
    # name = input("Name:")
    # lib.register_patron(name, (ord(name[0]) + len(name)))
    command = display_commands()
    while command != 'exit':
        if command == "show":
            print('Books: ')
            for book in books:
                print(book)
        elif command == 'patrons':
            print('Patrons: ')
            for patron in patronslist:
                print(patron.name, patron.patron_id)
        elif command == 'instock':
            books_available = lib.books_available
            for book in books_available:
                print(book)
        elif command == 'outstock':
            books_unavailable = [object for object in books if object not in books_available]
            for book in books_unavailable:
                print(book)
        elif command == 'add':
            lib.add_book(input('Title: '), input('Author: '), input('Genre: '), True)
        elif command == 'register':
            lib.register_patron(input('Name: '), input('Id: '))
        elif command == 'get':
            cd.check_out(input("Name of the book you want to check out : "))
        elif command == 'return':
            cd.return_book(input("Name of the book you want to return: "))
        else:
            print("Invalid input")
        command = display_commands()


if __name__ == '__main__':
    main()
