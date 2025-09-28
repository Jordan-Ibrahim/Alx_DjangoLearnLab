from django.contrib import admin
from django.urls import path
from .views import BookListCreateView, BookDetailView
   
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]