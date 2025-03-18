from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post,Tag
from .models import Comment
from taggit.forms import TagWidget  # Import the TagWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include tags in the form

    # Explicitly set the widget for the tags field
    tags = forms.CharField(
        required=False,
        widget=TagWidget()  # This is the TagWidget that handles the tag input
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Write a comment...'})

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
