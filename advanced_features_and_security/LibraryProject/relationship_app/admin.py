from django.contrib import admin
from .models import Author, Book, Library, Librarian
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'profile_photo', 'is_staff']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo'),
        }),
    )
    search_fields = ['username', 'email']
    ordering = ['username']

admin.site.register(CustomUser, CustomUserAdmin)



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
