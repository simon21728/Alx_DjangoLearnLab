# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    # Query all books by a specific author
    author = Author.objects.get(name=author_name)
    books = author.books.all()  # Using the related_name 'books'
    for book in books:
        print(f"Book: {book.title}")

def list_books_in_library(library_name):
    # List all books in a specific library
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(f"Book: {book.title}")

def retrieve_librarian_for_library(library_name):
    # Retrieve the librarian for a specific library
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"Librarian for {library_name}: {librarian.name}")

if __name__ == "__main__":
    # Example queries:
    query_books_by_author("J.K. Rowling")
    list_books_in_library("Central Library")
    retrieve_librarian_for_library("Central Library")
