from rest_framework import serializers
from .models import Author, Book
# BookSerializer serializes all fields of the Book model and includes custom validation for publication_year.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation for the publication year
    def validate_publication_year(self, value):
        if value > 2025:  # Assuming 2025 is the current year or the latest allowed publication year
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
# AuthorSerializer serializes the Author model and includes a nested BookSerializer to handle related books.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
