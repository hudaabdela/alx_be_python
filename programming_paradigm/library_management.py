class Book:
    def __init__(self, title: str, author: str):
        self.title = title        # Public attribute for the title
        self.author = author      # Public attribute for the author
        self._is_checked_out = False  # Private attribute for checkout status

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # Private list to store books

    def add_book(self, book: Book):
        self._books.append(book)

    def check_out_book(self, title: str):
        for book in self._books:
            if book.title == title and book.check_out():
                return True
        return False

    def return_book(self, title: str):
        for book in self._books:
            if book.title == title and book.return_book():
                return True
        return False

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(book)

