class Ebook:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.current_page = None
        self.is_open = False

    def open_book(self):
        if not self.is_open:
            self.is_open = True
            self.current_page = 1
            print(f"The book '{self.title}' is now open.")
        else:
            print(f"The book '{self.title}' is already open.")

    def close_book(self):
        if self.is_open:
            self.is_open = False
            self.current_page = None
            print(f"The book '{self.title}' is now closed.")
        else:
            print(f"The book '{self.title}' is already closed.")

    def next_page(self):
        if self.is_open:
            if self.current_page < self.num_pages:
                self.current_page += 1
                print(f"Moved to page {self.current_page}.")
            else:
                print("You are already on the last page.")
        else:
            print("Cannot turn the page. The book is closed.")

    def previous_page(self):
        if self.is_open:
            if self.current_page > 1:
                self.current_page -= 1
                print(f"Moved to page {self.current_page}.")
            else:
                print("You are already on the first page.")
        else:
            print("Cannot turn the page. The book is closed.")

    def display_status(self):
        if self.is_open:
            print(f"Book: '{self.title}' by {self.author}, Pages: {self.num_pages}, Current Page: {self.current_page}")
        else:
            print(f"Book: '{self.title}' by {self.author}, Pages: {self.num_pages}. The book is closed.")



def main():
    # Create an Ebook object
    my_book = Ebook("Python Programming", "John Doe", 250)

    # Open the book
    my_book.open_book()

    # Display book status
    my_book.display_status()

    # Read a few pages
    my_book.next_page()
    my_book.next_page()
    my_book.display_status()

    # Go back a page
    my_book.previous_page()
    my_book.display_status()

    # Close the book
    my_book.close_book()

    # Attempt to read a page while the book is closed
    my_book.next_page()

if __name__ == "__main__":
    main()
