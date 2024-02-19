import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.borrowed = False
        self.borrower = None
        self.borrow_date = None

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Library")

        self.books = [
            Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"),
            Book("To Kill a Mockingbird", "Harper Lee", "Fiction"),
            Book("1984", "George Orwell", "Fiction"),
            Book("The Hobbit", "J.R.R. Tolkien", "Fantasy"),
            Book("The Catcher in the Rye", "J.D. Salinger", "Fiction"),
            Book("The Da Vinci Code", "Dan Brown", "Thriller"),
            Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Fantasy"),
            Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Science Fiction"),
            Book("The Hunger Games", "Suzanne Collins", "Young Adult"),
            Book("Garfield: Fat Cat Pack", "Jim Davis", "Comic"),
            Book("Meteorite Strike", "A. G. Taylor", "Science Fiction"),
            Book("Ready Player One", "Ernest Cline", "Science Fiction"),
            Book("The Silver Eyes", "Scott Cawthon", "Horror"),
            Book("Around the World in Eighty Days", "Jules Verne", "Fiction"),
            Book("Charlie and the Chocolate Factory", "Roald Dahl", "Fiction"),
            Book("Diary of a Wimpy Kid", "Jeff Kinney", "Comic"),
        ]

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Welcome to the Book Library", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.genre_label = tk.Label(self.root, text="Select Genre:")
        self.genre_label.pack()

        self.genre_var = tk.StringVar()
        self.genre_var.set("All")

        self.genre_options = ["All"] + list(set(book.genre for book in self.books))
        self.genre_menu = tk.OptionMenu(self.root, self.genre_var, *self.genre_options, command=self.filter_books)
        self.genre_menu.pack()

        self.book_listbox = tk.Listbox(self.root, height=10, width=100)
        self.book_listbox.pack(pady=10)

        self.update_book_list()

        self.borrow_button = tk.Button(self.root, text="Borrow Book", command=self.borrow_book)
        self.borrow_button.pack()

        self.return_button = tk.Button(self.root, text="Return Book", command=self.return_book)
        self.return_button.pack()

    def update_book_list(self):
        self.book_listbox.delete(0, tk.END)
        selected_genre = self.genre_var.get()
        if selected_genre == "All":
            books_to_display = self.books
        else:
            books_to_display = [book for book in self.books if book.genre == selected_genre]
        for book in books_to_display:
            status = "Available" if not book.borrowed else f"Borrowed by {book.borrower}"
            self.book_listbox.insert(tk.END, f"{book.title} by {book.author} ({status})")

    def filter_books(self, event=None):
        self.update_book_list()

    def borrow_book(self):
        selected_index = self.book_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a book to borrow.")
            return
        selected_book = self.books[selected_index[0]]
        if selected_book.borrowed:
            messagebox.showerror("Error", "This book is already borrowed.")
            return
        selected_book.borrowed = True
        selected_book.borrower = "Toma" 
        selected_book.borrow_date = datetime.now()
        return_date = selected_book.borrow_date + timedelta(days=14)
        messagebox.showinfo("Success", f"You have successfully borrowed {selected_book.title}.\nPlease return by {return_date.strftime('%Y-%m-%d')}")
        self.update_book_list()

    def return_book(self):
        selected_index = self.book_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a book to return.")
            return
        selected_book = self.books[selected_index[0]]
        if not selected_book.borrowed:
            messagebox.showerror("Error", "This book is not currently borrowed.")
            return
        selected_book.borrowed = False
        selected_book.borrower = None
        selected_book.borrow_date = None
        messagebox.showinfo("Success", f"You have successfully returned {selected_book.title}.")
        self.update_book_list()

def main():
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
