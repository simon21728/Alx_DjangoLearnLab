# bookshelf/forms.py
from django import forms

class BookForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        # Additional validation logic (e.g., checking for prohibited characters)
        return title
