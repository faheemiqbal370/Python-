from datetime import datetime, timedelta

class Library:
    def __init__(self):

        self.books = {
            "Python": True,
            "C++": True,
            "Java": True,
            "DBMS": True,
            "OS": True
        }
        self.issued = {}     


    def view_available(self):
        print("\nAvailable Books:")
        for book, status in self.books.items():
            if status:
                print(" -", book)


    def issue_book(self, book):
        if book in self.books and self.books[book]:
            self.books[book] = False
            self.issued[book] = datetime.now()
            print(f"\n✔ '{book}' issued successfully!")
        else:
            print("\n✖ Book not available or doesn't exist.")


    def return_book(self, book):
        if book in self.issued:
            issued_date = self.issued.pop(book)
            self.books[book] = True

            days = (datetime.now() - issued_date).days
            if days > 15:
                fine = days - 15
                print(f"\nBook returned. Fine to pay: ₹{fine}")
            else:
                print("\n✔ Book returned. No fine.")
        else:
            print("\n✖ This book was not issued.")


    def check_list(self):
        print("\nIssued Books:")
        if not self.issued:
            print("No books issued.")
        else:
            for book, date in self.issued.items():
                print(f"{book} -> issued on {date.strftime('%d-%m-%Y')}")




def main():
    lib = Library()

    while True:
        print("""
1. Issue a Book
2. Return a Book
3. Check Issued Book List
4. View Available Books
0. Exit
""")

        choice = input("Enter choice: ")

        if choice == "1":
            lib.issue_book(input("Enter book name: "))
        elif choice == "2":
            lib.return_book(input("Enter book name: "))
        elif choice == "3":
            lib.check_list()
        elif choice == "4":
            lib.view_available()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

main()
