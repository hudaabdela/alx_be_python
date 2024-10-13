# library_system.py

# Base class: Book
class Book:
    def __init__(self, title, author):
        #Initializes a book with a title and author.
        self.title = title
        self.author = author

    def __str__(self):
        #Returns a string representation of the book.
        return f"{self.title} by {self.author}"

# Derived class: EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        #Initializes an eBook with a title, author, and file size.
        super().__init__(title, author)  # Calls the base class (Book) constructor
        self.file_size = file_size

    def __str__(self):
        #Returns a string representation of the eBook.
        return f"{self.title} by {self.author} [EBook: {self.file_size} MB]"

# Derived class: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        #Initializes a print book with a title, author, and page count.
        super().__init__(title, author)  # Calls the base class (Book) constructor
        self.page_count = page_count

    def __str__(self):
        #Returns a string representation of the print book.
        return f"{self.title} by {self.author} [PrintBook: {self.page_count} pages]"

# Composition class: Library
class Library:
    def __init__(self):
        #Initializes the library with an empty collection of books.
        self.books = []

    def add_book(self, book):
        #Adds a book (Book, EBook, or PrintBook) to the library.
        self.books.append(book)

    def list_books(self):
        #Prints the details of all books in the library.
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)
