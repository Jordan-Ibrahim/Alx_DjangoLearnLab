# api/test_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):
    """Tests for Book API endpoints including CRUD, filtering, search, ordering, and permissions."""

    def setUp(self):
        """
        Create sample data and an authenticated user for permission testing.
        This runs before each test method.
        """
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        self.author = Author.objects.create(name='Chinua Achebe')
        self.book = Book.objects.create(
            title='Things Fall Apart',
            publication_year=1958,
            author=self.author
        )

        self.list_url = reverse('book-list')  # defined in your urls.py
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})

    def test_list_books(self):
        """Test retrieving all books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)  # at least one book

    def test_create_book(self):
        """Test creating a new book."""
        data = {
            'title': 'No Longer at Ease',
            'publication_year': 1960,
            'author': self.author.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_retrieve_book_detail(self):
        """Test retrieving a single book by ID."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Things Fall Apart')

    def test_update_book(self):
        """Test updating an existing book."""
        data = {
            'title': 'Things Fall Apart (Updated)',
            'publication_year': 1958,
            'author': self.author.id
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Things Fall Apart (Updated)')

    def test_delete_book(self):
        """Test deleting a book."""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_publication_year(self):
        """Test filtering books by publication_year."""
        response = self.client.get(self.list_url, {'publication_year': 1958})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book['publication_year'] == 1958 for book in response.data))

    def test_search_books_by_title(self):
        """Test searching books by title."""
        response = self.client.get(self.list_url, {'search': 'Things'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_order_books_by_publication_year(self):
        """Test ordering books by publication_year."""
        # create another book with later year
        Book.objects.create(title='Anthills of the Savannah', publication_year=1987, author=self.author)