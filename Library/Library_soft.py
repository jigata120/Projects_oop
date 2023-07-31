# Class representing a book with its properties like title, author, genre, and availability.
class Book:
    def __init__(self, title, author, genre, availability):
        self.title = title
        self.author = author
        self.genre = genre
        self.availability = availability

    def __str__(self):
        # Returns a formatted string representation of the book, including its availability status.
        return f'{self.title} by {self.author} |{self.genre}|-{"Available" if self.availability else "Unavailable"}'


# Class representing a patron with their name and patron ID.
class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id


# Class representing a library with books, patrons, and methods to add books and register patrons.
class Library:
    def __init__(self):
        self.all_books = []         # List to store all the books in the library.
        self.patrons = []           # List to store all the registered patrons.
        self.books_available = []   # List to store books that are currently available.

    def add_book(self, title, author, genre, availability):
        # Adds a new book to the library with the given details and availability status.
        title = Book(title, author, genre, availability)
        self.all_books.append(title)
        if title.availability:
            self.books_available.append(title)

    def register_patron(self, name, patron_id):
        # Registers a new patron with the given name and patron ID.
        patron_id = Patron(name, patron_id)
        self.patrons.append(patron_id)
        return patron_id


# Class representing search operations in the library (not implemented in the provided code).
class Search:
    def search_for_available(self):
        # Performs a search for available books.
        ...

    def search_for_book(self):
        # Performs a search for a specific book.
        ...


# Class representing methods for checking out and returning books.
class Methods:
    def check_out(self, book_):
        # Checks out a book by setting its availability to False and updating the books_available list.
        for object in books:
            if object.title == book_:
                object.availability = False
                if object in books_available:
                    lib.books_available.remove(object)

    def return_book(self, book_):
        # Returns a book by setting its availability to True and updating the books_available list.
        for object in books:
            if object.title == book_:
                object.availability = True
                if object not in books_available:
                    lib.books_available.append(object)


# Instantiate the Library class.
lib = Library()

# Instantiate the Methods class to use check_out and return_book functions.
cd = Methods()

# Add some sample books and register patrons to initialize the library.
lib.add_book('HarryPotter', 'Jonh Crhis', 'fantasy', True)
lib.add_book('Rich dad poor dad', 'Sakato Nakamura', 'Business', False)
lib.add_book('The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', True)
lib.add_book('To Kill a Mockingbird', 'Harper Lee', 'Classics', True)
lib.add_book('1984', 'George Orwell', 'Dystopian', False)
lib.add_book('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', False)

lib.register_patron('Sam', 188)
lib.register_patron('Nick', 127)
lib.register_patron('Mike', 257)

# Get references to the library's books, patrons, and available books for later use.
books = lib.all_books
patronslist = lib.patrons
books_available = lib.books_available

# Function to display available commands and retrieve user input.
def display_commands():
    ...

# The main function to run the library management system.
def main():
    ...


if __name__ == '__main__':
    main()
