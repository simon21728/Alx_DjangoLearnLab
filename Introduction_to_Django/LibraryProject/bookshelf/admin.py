# bookshelf/admin.py
from django.contrib import admin
from .models import Book  # Import the Book model

class BookAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

# Register the Book model along with the BookAdmin configuration
admin.site.register(Book, BookAdmin)
=======
    list_display = ('title', 'author', 'publication_date')  # Fields to display in the list view
    list_filter = ('publication_date',)  # Add publication_year to the list filters
    search_fields = ('title', 'author')  # Optional: Add search functionality
     
>>>>>>> f1667d18cc1419c37d2be551cd70c57737cf6181
