# bookshelf/models.py

from django.db import models

# Author model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book model (Notice how we're using a string reference here)
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()  # Make sure this field is defined here

    def __str__(self):
        return self.title

