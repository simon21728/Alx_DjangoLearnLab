from django.contrib import admin

from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author')
    
    # Filter by year
    list_filter = ('published_date',)
    
    def get_published_year(self, obj):
        return obj.published_date.year
    get_published_year.admin_order_field = 'published_date'  # Allows sorting by year
    get_published_year.short_description = 'Publication Year'

admin.site.register(Book, BookAdmin)

