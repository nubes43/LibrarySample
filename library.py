from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f'Book "{title}" by {author} added to the library.')

    def borrow_book(self, title, copy_index):
        if copy_index < 0 or copy_index >= len(self.books):
            print('Invalid copy index')
            return
        book = self.books[copy_index]
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
