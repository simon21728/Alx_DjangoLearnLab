from django.contrib import admin
from .models import Author, Book, Library, Librarian

# Register your models here.



# Customizing the Admin for Author Model
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the author's name in the list view
    search_fields = ('name',)  # Allow search by name

admin.site.register(Author, AuthorAdmin)

# Customizing the Admin for Book Model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')  # Display book title and author in the list view
    search_fields = ('title', 'author__name')  # Allow search by title or author's name
    list_filter = ('author',)  # Add a filter for the author in the admin view

admin.site.register(Book, BookAdmin)

# Customizing the Admin for Library Model
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display library name in the list view
    search_fields = ('name',)  # Allow search by library name
    filter_horizontal = ('books',)  # Add a horizontal filter for selecting books

admin.site.register(Library, LibraryAdmin)

# Customizing the Admin for Librarian Model
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', 'library')  # Display librarian name and the associated library
    search_fields = ('name', 'library__name')  # Allow search by librarian name or library name

admin.site.register(Librarian, LibrarianAdmin)
