class Book:
    def __init__(self, book_title, author, book_id,):
        self.book_title = book_title
        self.author = author
        self.book_id = book_id
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        self.is_available = True

    def display_details(self):
        status = "Available" if self.is_available else "Borrowed"
        print(f"Book ID: {self.book_id}, Title: {self.book_title}, Author: {self.author}, Status: {status}")


class Member:
    def __init__(self, member_name, member_id):
        self.member_name = member_name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book_id):
        self.borrowed_books.append(book_id)

    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)

    def display_borrowed_books(self):
        print(f"{self.member_name} (ID: {self.member_id}) borrowed books: {', '.join(self.borrowed_books) if self.borrowed_books else 'None'}")


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book_title, author, book_id):
        if book_id not in self.books:
            self.books[book_id] = Book(book_title, author, book_id)
            print("Book added successfully.")
        else:
            print("Book ID already exists.")

    def register_member(self, member_name, member_id):
        if member_id not in self.members:
            self.members[member_id] = Member(member_name, member_id)
            print("Member registered successfully.")
        else:
            print("Member ID already exists.")

    def borrow_book(self, member_id, book_id):
        if member_id in self.members and book_id in self.books:
            book = self.books[book_id]
            if book.borrow():
                self.members[member_id].borrow_book(book_id)
                print("Book borrowed successfully.")
            else:
                print("Book is already borrowed.")
        else:
            print("Invalid member ID or book ID.")

    def return_book(self, member_id, book_id):
        if member_id in self.members and book_id in self.books:
            book = self.books[book_id]
            if book_id in self.members[member_id].borrowed_books:
                book.return_book()
                self.members[member_id].return_book(book_id)
                print("Book returned successfully.")
            else:
                print("This member didn't borrow this book.")
        else:
            print("Invalid member ID or book ID.")

    def display_all_books(self):
        print("\nLibrary Books:")
        for book in self.books.values():
            book.display_details()

    def display_all_members(self):
        print("\nLibrary Members:")
        for member in self.members.values():
            member.display_borrowed_books()


# Main program
def main():
    library = Library()
    while True:
        print("\nIBM Library Management System")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. List All Books")
        print("6. List All Members")
        print("7. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            book_id = input("Enter book ID: ")
            library.add_book(title, author, book_id)
        
        elif choice == "2":
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            library.register_member(name, member_id)
        
        elif choice == "3":
            member_id = input("Enter member ID: ")
            book_id = input("Enter book ID: ")
            library.borrow_book(member_id, book_id)
        
        elif choice == "4":
            member_id = input("Enter member ID: ")
            book_id = input("Enter book ID: ")
            library.return_book(member_id, book_id)
        
        elif choice == "5":
            library.display_all_books()
        
        elif choice == "6":
            library.display_all_members()
        
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
