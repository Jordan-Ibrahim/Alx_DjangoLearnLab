from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='libraries')
    def __str__(self):
        return self.name    

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library,on_delete=models.CASCADE, related_name='librarian')
    def __str__(self):
        return self.name

class UserProfile (models.Model):
    role = models.CharField('Admion/Librarian/Member', max_length=200)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username