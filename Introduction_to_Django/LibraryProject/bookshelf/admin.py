from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')  # Fields to display in the list view
    list_filter = ('publication_date',)  # Add publication_year to the list filters
    search_fields = ('title', 'author')  # Optional: Add search functionality
     
