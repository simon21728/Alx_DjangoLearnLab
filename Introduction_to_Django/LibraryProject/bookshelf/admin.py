from django.contrib import admin

# Register your models here.
# bookshelf/admin.py
from django.contrib import admin
from .models import Book
class BookAdmin(admin.ModelAdmin):
    # Specify which fields to display in the list view
    list_display = ('title', 'author', 'published_date')

    # Add search functionality for title and author fields
    search_fields = ('title', 'author')

    # Add filter options based on publication year
    list_filter = ('published_date',)

# Register the Book model with the default admin interface
admin.site.register(Book,BookAdmin)
