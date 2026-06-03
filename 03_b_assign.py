class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'"{book}" added successfully.')

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'"{book}" removed successfully.')
        else:
            print("Book not found!")

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'"{book}" issued successfully.')
        else:
            print("Book not available!")

    def return_book(self, book):
        self.books.append(book)
        print(f'"{book}" returned successfully.')

    def display_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("\nAvailable Books:")
            for book in self.books:
                print("-", book)


library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        library.add_book(book)

    elif choice == "2":
        book = input("Enter book name to remove: ")
        library.remove_book(book)

    elif choice == "3":
        book = input("Enter book name to issue: ")
        library.issue_book(book)

    elif choice == "4":
        book = input("Enter book name to return: ")
        library.return_book(book)

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        print("Exiting Library System...")
        break

    else:
        print("Invalid choice!")