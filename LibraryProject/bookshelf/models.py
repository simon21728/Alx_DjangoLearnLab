from django.db import models
from .models import Book

# bookshelf/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()  # This is likely the field you are referring to
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    language = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title



book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)


book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")


book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()


book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()