from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f'Book "{title}" by {author} added to the library.')

    def borrow_book(self, title, index=0):
        # Find all matching books by title
        matching_books = [book for book in self.books if book.title == title]
        if index < len(matching_books):
            book = matching_books[index]
            if book.borrow():
                print(f'You have borrowed "{title}" (Copy {index + 1}).')
                return
            else:
                print(f'Sorry, "{title}" (Copy {index + 1}) is currently borrowed.')
                return
        print(f'Sorry, "{title}" is not available in the library.')

    def return_book(self, title, index=0):
        # Find all matching books by title
        matching_books = [book for book in self.books if book.title == title]
        if index < len(matching_books):
            book = matching_books[index]
            if book.return_book():
                print(f'You have returned "{title}" (Copy {index + 1}).')
                return
            else:
                print(f'Error: "{title}" (Copy {index + 1}) was not borrowed.')
                return
        print(f'Sorry, "{title}" is not recognized by the library.')
>>> NEW

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f'Book "{title}" by {author} added to the library.')

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.borrow():
                    print(f'You have borrowed "{title}".')
                    return
                else:
                    print(f'Sorry, "{title}" is currently borrowed.')
                    return
        print(f'Sorry, "{title}" is not available in the library.')

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.return_book():
                    print(f'You have returned "{title}".')
                    return
                else:
                    print(f'Error: "{title}" was not borrowed.')
                    return
        print(f'Sorry, "{title}" is not recognized by the library.')
