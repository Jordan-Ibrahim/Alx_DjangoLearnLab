from django.urls import path
from .views import (
    BookListView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),                  # GET all books
    path('books/create/', BookCreateView.as_view(), name='book-create'),       # POST create
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'), # PUT/PATCH update
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'), # DELETE delete
]