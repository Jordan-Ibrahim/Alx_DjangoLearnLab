from django.contrib import admin
from django.urls import path
from .views import list_books
from . import views
from .views import RegisterView as SignUpView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.list_books, name='list-books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
    path("register/", views.register(), name="register"),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path("logout/", LogoutView.as_view(template_name='relationship_app/logout.html'), name="logout"),
]
