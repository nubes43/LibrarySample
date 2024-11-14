from library import Library

def main():
    library = Library()

    while True:
        print("\nLibrary System")
        print("1. Add a book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == '2':
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)
        elif choice == '3':
            title = input("Enter book title to return: ")
            library.return_book(title)
        elif choice == '4':
            print("Exiting the library system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
