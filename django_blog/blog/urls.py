from django.contrib import admin
from django.urls import path, include
from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views
from views import SignUpView, profile_view, PostDetailView, add_comment, CommentEditView, CommentDeleteView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path("post/", views.PostListView.as_view(), name='post_list'),
    path("post/new/", views.PostCreateView.as_view(), name='post_create'),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name='post_detail'),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name='post_update'),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name='post_delete'),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", SignUpView.as_view(), name="register"),
    path("profile/", profile_view, name="profile"),
    path('posts/<int:pk>/comment/new/', add_comment, name='add_comment'),
    path('comment/<int:pk>/edit/', CommentEditView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),

]