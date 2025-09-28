from django.db import models

# Create your models here.

# Author model: represents a writer who can have multiple books
class Author(models.Model):
    name = models.CharField(max_length=200)  # Name of the author

    def __str__(self):
        return self.name


# Book model: represents an individual book written by an Author
class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    publication_year = models.IntegerField()  # Year the book was published

    # ForeignKey creates a one-to-many relationship: One Author → Many Books
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'  # Allows author.books.all() to fetch all books
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

