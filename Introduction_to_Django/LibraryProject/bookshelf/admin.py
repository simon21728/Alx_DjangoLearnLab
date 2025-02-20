# bookshelf/admin.py
from django.contrib import admin
from .models import Book  # Import the Book model

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

# Register the Book model along with the BookAdmin configuration
admin.site.register(Book, BookAdmin)
