from django.contrib import admin
from django.urls import path
from .views import list_books
from . import views
from .views import SignUpView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.list_books, name='list-books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]