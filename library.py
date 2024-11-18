from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f'Book "{title}" by {author} added to the library.')

    def borrow_book(self, title, book_id):
        for book in self.books:
            if book.title == title and book.id == book_id:
                if book.borrow():
                    print(f'You have borrowed "{title}" (ID: {book_id}).')
                    return
                else:
                    print(f'Sorry, "{title}" (ID: {book_id}) is currently borrowed.')
                    return
        print(f'Sorry, "{title}" with ID {book_id} is not available in the library.')

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
