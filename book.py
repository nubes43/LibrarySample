class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        else:
            return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        else:
            return False
