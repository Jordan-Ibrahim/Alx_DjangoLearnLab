from django.contrib import admin
from django.urls import path, include
from api.views import BookViewset
from rest_framework import routers

# Router instance
router = routers.DefaultRouter()
router.register(r'books', BookViewset, basename='book')  # simpler name

urlpatterns = [
    
    path('', include(router.urls)),  # includes all CRUD endpoints
]

