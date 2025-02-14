from django.db import models

from bookshelf.models import Book

# Create a new Book instance
new_book = Book.objects.create(
    title="1984",  # Book Title
    author="George Orwell",  # Book Author
    published_date="1949-06-08",  # Date when the book was published
    isbn="9780451524935",  # ISBN number for the book
    pages=328,  # Number of pages
    language="English"  # Language of the book
)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

books = Book.objects.all()
print(books)
