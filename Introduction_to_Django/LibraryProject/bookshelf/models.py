# bookshelf/models.py

from django.db import models

# Author model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book model (Notice how we're using a string reference here)
class Book(models.Model):
<<<<<<< HEAD
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f'{self.title} by {self.author} ({self.publication_year})'
=======
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()  # Make sure this field is defined here

    def __str__(self):
        return self.title

>>>>>>> f1667d18cc1419c37d2be551cd70c57737cf6181
