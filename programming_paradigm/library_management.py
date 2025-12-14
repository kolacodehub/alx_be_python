class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    # print(f"You have checked out '{title}'.")
                    return
                else:
                    # print(f"Sorry, '{title}' is already checked out.")
                    return
        print(f"Could not find book: {title}")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    # print(f"You have returned '{title}'.")
                    return
                else:
                    # print(f"'{title}' was not checked out.")
                    return
        print(f"Could not find book: {title}")

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
               print(f"{book.title} by {book.author}")