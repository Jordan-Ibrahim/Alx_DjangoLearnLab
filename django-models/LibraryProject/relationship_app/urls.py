from django.contrib import admin
from django.urls import path
from .views import list_books
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.list_books, name='list-books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
]