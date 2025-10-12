from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        # used by CreateView/UpdateView by default for redirect after save
        return reverse('blog:post_detail', kwargs={'pk': self.pk})
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']   # oldest first; change to '-created_at' if you want newest first

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'



