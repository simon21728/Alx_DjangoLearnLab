from django.contrib import admin

# bookshelf/admin.py
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Specify which fields to display in the list view
    list_display = ('title', 'author', 'published_date')
    
    # Enable search functionality for title and author fields
    search_fields = ('title', 'author')

    # Configure the filter options: Filter by published date (year)
    list_filter = ('published_date',)

admin.site.register(Book, BookAdmin)
