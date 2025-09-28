from django.contrib import admin
from django.urls import path, include
from api.views import BookViewset
from rest_framework import routers
from .views import BookList

# Router instance
router = routers.DefaultRouter()
router.register(r'books', BookViewset, basename='book')  # simpler name

urlpatterns = [
    
    path('', include(router.urls)),
    path('books/', BookList.as_view(), name='book-list') # includes all CRUD endpoints
]

