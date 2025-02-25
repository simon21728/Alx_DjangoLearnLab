# bookshelf/forms.py
from django import forms

class BookForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        # Additional validation logic (e.g., checking for prohibited characters)
        return title
# bookshelf/forms.py

from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, label="Book Title")
    author = forms.CharField(max_length=100, required=True, label="Author")

    def clean_title(self):
        title = self.cleaned_data.get('title')
        # Add custom validation logic for title, e.g., no special characters
        if not title.isalnum():
            raise forms.ValidationError("Title should only contain letters and numbers.")
        return title

    def clean_author(self):
        author = self.cleaned_data.get('author')
        # Example custom validation for author field
        if len(author) < 3:
            raise forms.ValidationError("Author name must be at least 3 characters long.")
        return author
