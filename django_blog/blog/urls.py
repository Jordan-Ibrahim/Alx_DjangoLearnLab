from django.contrib import admin
from django.urls import path, include
from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views
from blog import SignUpView, profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path("post/", views.PostListView.as_view(), name='post_list'),
    path("post/new/", views.PostCreateView.as_view(), name='post_create'),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name='post_detail'),
    path("post/<int:pk>/edit/", views.PostUpdateView.as_view(), name='post_update'),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name='post_delete'),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", SignUpView.as_view(), name="register"),
    path("profile/", profile_view, name="profile"),

]