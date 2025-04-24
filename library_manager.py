import json
import os


file_data = "library.txt"

def load_data():
    if os.path.exists(file_data):
        with open(file_data, "r") as file:
            return json.load(file)
        
    return[]

def save_data(data):
    with open(file_data, "w") as file:
        json.dump(data, file, indent=4)



def add_book(data):
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    genre = input("Enter the book genre: ")
    year = input("Enter the book publication year: ")
    read = input("Have you read this book? (yes/no): ").lower() == "yes"


    book = {
        "title": title,
        "author": author,
        "genre": genre,
        "year": year,
        "read": read
    }  

    data.append(book)
    save_data(data)
    print(f"Book {title} added successfully!")


def remove_book(data):
    title = input("Enter the book title to remove: ")
    initial_length = len(data)
    data = [book for book in data if book["title"].lower() != title.lower()]
    if len(data) < initial_length:
        save_data(data)
        print(f"Book {title} removed successfully!")
    else:
        print(f"Book {title} not found in the library.")


def search_books(data):
    search_by = input("Search by (title/author): ").strip().lower()

    # Check if input is valid
    if search_by not in ["title", "author"]:
        print("❌ Invalid search type. Please enter only 'title' or 'author'.")
        return

    search_term = input(f"Enter the {search_by}: ").strip().lower()
    
    result = [book for book in data if search_term in book[search_by].lower()]

    if result:
        for book in result:
            status = "Read" if book["read"] else "Not Read"
            print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Year: {book['year']}, Status: {status}")
    else:
        print(f"🔍 No books found for {search_by}: {search_term}")


def list_books(data):
    if data:
        for book in data:
            status = "Read" if book["read"] else "Not Read"
            print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Year: {book['year']}, Status: {status}")
    else:
            print("No books in the library.")


def statistics(data):
    total_books = len(data)
    read_books = len([book for book in data if book["read"]])
    unread_books = total_books - read_books
    read_percentage = (read_books / total_books) * 100 if total_books > 0 else 0
    unread_percentage = (unread_books / total_books) * 100 if total_books > 0 else 0

    print(f"Total books: {total_books}")
    print(f"Books read: {read_books}")
    print(f"Books not read: {read_percentage: .1f}%")
    print(f"Books read: {unread_books: .1f}%")


def main():
    data = load_data()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Books")
        print("4. List Books")
        print("5. Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(data)
        elif choice == "2":
            remove_book(data)
        elif choice == "3":
            search_books(data)
        elif choice == "4":
            list_books(data)
        elif choice == "5":
            statistics(data)
        elif choice == "6":
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
        main()
# This code is a simple library management system that allows users to add, remove, search, list books, and view statistics about their library.        




