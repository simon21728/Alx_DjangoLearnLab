# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Get all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()  # Using the reverse relation defined by related_name='books'
    for book in books:
        print(book.title)

# Query 2: List all books in a specific library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # Using the reverse relation defined by related_name='libraries'
    for book in books:
        print(book.title)

# Query 3: Retrieve the librarian for a specific library
def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian  # Using the reverse relation defined by related_name='librarian'
    print(librarian.name)

# Test the queries
if __name__ == '__main__':
    print("Books by Author 'J.K. Rowling':")
    books_by_author('J.K. Rowling')
    
    print("\nBooks in 'Central Library':")
    books_in_library('Central Library')
    
    print("\nLibrarian of 'Central Library':")
    librarian_of_library('Central Library')
def get_books_by_author(author_name):
    try:
        # Get the author by name
        author = Author.objects.get(name=author_name)
        
        # Filter books by the retrieved author
        books = Book.objects.filter(author=author)
        
        # Print the books' titles for this author
        for book in books:
            print(f"Book Title: {book.title}")
    
    except Author.DoesNotExist:
        print(f"No author found with the name {author_name}")

# Example Usage
get_books_by_author("Author Name")
def get_librarian_by_library(library_name):
    try:
        # Get the library by name
        library = Library.objects.get(name=library_name)
        
        # Get the librarian associated with that library
        librarian = Librarian.objects.get(library=library)
        
        # Print librarian details
        print(f"Librarian: {librarian.name} works at {library.name} library.")
    
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for the library {library_name}")

# Example usage
get_librarian_by_library("Central Library")  # Replace with an actual library name