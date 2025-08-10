class Book:
    """A base class representing a generic book."""
    def __init__(self, title, author):
        """Initializes a Book instance."""
        self.title = title
        self.author = author

class EBook(Book):
    """A class representing an electronic book, inheriting from Book."""
    def __init__(self, title, author, file_size):
        """Initializes an EBook instance, calling the parent constructor."""
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    """A class representing a physical book, inheriting from Book."""
    def __init__(self, title, author, page_count):
        """Initializes a PrintBook instance, calling the parent constructor."""
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    """A class representing a library that manages a collection of books."""
    def __init__(self):
        """Initializes a Library instance with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Adds a book instance to the library's collection."""
        self.books.append(book)

    def list_books(self):
        """Prints the details of each book in the library."""
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")