from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)  # author’s name

    def __str__(self):
        return self.name  # makes admin and shell more readable


class Book(models.Model):
    title = models.CharField(max_length=200)  # book’s title
    publication_year = models.IntegerField()  # publication year
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'  # allows author.books.all() to work
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"