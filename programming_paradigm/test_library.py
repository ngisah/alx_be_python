from library_management import Book, Library

def test_book_class():
    """Test the Book class functionality."""
    print("Testing Book class:")
    
    # Create a book
    book = Book("Test Book", "Test Author")
    print(f"Book created: {book.title} by {book.author}")
    print(f"Initially available: {book.is_available()}")
    
    # Check out the book
    book.check_out()
    print(f"After checkout: {book.is_available()}")
    
    # Return the book
    book.return_book()
    print(f"After return: {book.is_available()}")
    print()

def test_library_class():
    """Test the Library class functionality."""
    print("Testing Library class:")
    
    # Create library and add books
    library = Library()
    library.add_book(Book("Book 1", "Author 1"))
    library.add_book(Book("Book 2", "Author 2"))
    
    print("Available books:")
    library.list_available_books()
    
    # Test checkout
    print("\nChecking out 'Book 1':")
    library.check_out_book("Book 1")
    library.list_available_books()
    
    # Test return
    print("\nReturning 'Book 1':")
    library.return_book("Book 1")
    library.list_available_books()

if __name__ == "__main__":
    test_book_class()
    test_library_class() 