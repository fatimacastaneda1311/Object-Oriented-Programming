# Create a class Book with attributes title and num_pages. Override:
# __str__() to print "Book: X, Pages: Y".
# __len__() so that len(book) returns the number of pages.

class Book:
    """Represents a book with a title and number of pages."""
    def __init__(self, title, num_pages):  # Initializes the Book object with a title and number of pages.
        self.title = title  # Sets the title of the book.
        self.pages = num_pages  # Sets the number of pages in the book.

    def __str__(self):  # Overrides the __str__ method to provide a string representation of the Book object.
        return f"Book: {self.title}, Pages: {self.pages}"  # Returns a formatted string with the book's title and number of pages.

    def __len__(self):  # Overrides the __len__ method to return the number of pages in the Book object.
        return self.pages  # Returns the number of pages in the book, allowing the use of len(book) to get this value.

# Testing the Book class and its overridden methods
book1 = Book("The Wizard of Oz", 211)  # Creates an instance of the Book class with the title "The Wizard of Oz" and 211 pages.
print(str(book1))  # Prints the string representation of book1, which is "Book: The Wizard of Oz, Pages: 211".
print(len(book1))  # Prints the number of pages in book1, which is 211.

book2 = Book("Little Women", 400)  # Creates another instance of the Book class with the title "Little Women" and 400 pages.
print(str(book2))  # Prints the string representation of book2, which is "Book: Little Women, Pages: 400".
print(len(book2))  # Prints the number of pages in book2, which is 400.

### POSSIBLE ERRORS (May occur if the code is modified incorrectly):
# 1. __str__() returns something that is not a string → always return str(...).
# 2. __len__() returns a non-integer or negative value → return int(self.pages) and validate that pages >= 0.
# 3. Confusion between __repr__ and __str__ → __repr__ should be more developer-oriented; __str__ should be user-oriented.