from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from relationship_app.models import UserProfile
from django.contrib.auth.models import Group, Permission

# Register Book model
admin.site.register(Book)

# Add custom permissions to groups
def assign_permissions():
    # Create groups
    group_admins, created = Group.objects.get_or_create(name='Admins')
    group_editors, created = Group.objects.get_or_create(name='Editors')
    group_viewers, created = Group.objects.get_or_create(name='Viewers')
    
    # Assign permissions to Admins group
    group_admins.permissions.set(
        Permission.objects.filter(content_type__model='book')
    )
    
    # Assign create and edit permissions to Editors group
    group_editors.permissions.set(
        Permission.objects.filter(codename__in=['can_create', 'can_edit'])
    )
    
    # Assign view permission to Viewers group
    group_viewers.permissions.set(
        Permission.objects.filter(codename='can_view')
    )

# Call this function once during app setup or manually from the shell to assign permissions.
assign_permissions()


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

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')  # Fields to display in the list view
    list_filter = ('publication_date',)  # Add publication_year to the list filters
    search_fields = ('title', 'author')  # Optional: Add search functionality
     
