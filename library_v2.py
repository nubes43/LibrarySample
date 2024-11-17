from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f'Book "{title}" by {author} added to the library.')

    def borrow_book(self, title):
        matching_books = [book for book in self.books if book.title == title]
        if not matching_books:
            print(f'Sorry, "{title}" is not available in the library.')
            return
        for i, book in enumerate(matching_books):
            if book.borrow():
                print(f'You have borrowed "{title}" (copy {i + 1}).')
                return
        print(f'Sorry, all copies of "{title}" are currently borrowed.')

    def return_book(self, title):
        matching_books = [book for book in self.books if book.title == title]
        if not matching_books:
            print(f'Sorry, "{title}" is not recognized by the library.')
            return
        for i, book in enumerate(matching_books):
            if book.return_book():
                print(f'You have returned "{title}" (copy {i + 1}).')
                return
        print(f'Error: All copies of "{title}" are currently available, none were borrowed.')