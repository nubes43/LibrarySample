class Book:
    _id_counter = 0  # Class variable to keep track of unique IDs

    def __init__(self, title, author):
        self.id = Book._id_counter  # Assign a unique ID
        Book._id_counter += 1  # Increment ID counter
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
