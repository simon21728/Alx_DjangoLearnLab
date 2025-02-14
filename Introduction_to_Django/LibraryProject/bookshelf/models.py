from django.db import models

from bookshelf.models import Book


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title


book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)


book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")


book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()


book_to_delete = Book.objects.get(id=1)
book_to_delete.delete()
