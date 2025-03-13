from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        """Set up initial data and users."""
        self.user = User.objects.create_user(username='sewmehon', password='Sew76@bayu21')
        self.book_data = {
            'title': 'Django for Beginners',
            'author': 'John Doe',
            'publication_year': '2023-01-01',
            'isbn': '1234567890'
        }
        self.book = Book.objects.create(**self.book_data)
        self.url = reverse('book-list')  # Assumes the name for the book list view is 'book-list'
    
    def test_create_book_authenticated(self):
        """Test that an authenticated user can create a book."""
        self.client.login(username='sewmehon', password='Sew76@bayu21')
        response = self.client.post(self.url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # Ensure one book is created

    def test_create_book_unauthenticated(self):
        """Test that an unauthenticated user cannot create a book."""
        response = self.client.post(self.url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book(self):
        """Test that an authenticated user can update a book."""
        update_data = {'title': 'Django for Experts'}
        self.client.login(username='sewmehon', password='Sew76@bayu')
        response = self.client.patch(reverse('book-detail', args=[self.book.id]), update_data, format='json')
        self.book.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.book.title, 'Django for Experts')

    def test_delete_book(self):
        """Test that an authenticated user can delete a book."""
        self.client.login(username='sewmehon', password='Sew76@bayu21')
        response = self.client.delete(reverse('book-detail', args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)  # Book should be deleted

    def test_book_list(self):
        """Test that a list of books can be retrieved."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one book exists in the DB

    def test_book_detail(self):
        """Test retrieving a single book."""
        response = self.client.get(reverse('book-detail', args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_filter_books(self):
        """Test filtering books by title and author."""
        response = self.client.get(self.url, {'title': 'Django for Beginners'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # One book should match the filter

    def test_search_books(self):
        """Test searching for books by title and author."""
        response = self.client.get(self.url, {'search': 'Django'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # The search should return the book

    def test_order_books(self):
        """Test ordering books by title and publication date."""
        book2 = Book.objects.create(
            title='Advanced Django',
            author='Jane Doe',
            publication_year='2022-01-01',
            isbn='0987654321'
        )
        response = self.client.get(self.url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Advanced Django')

        response = self.client.get(self.url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Django for Beginners')  # Since 'Django for Beginners' is newer
