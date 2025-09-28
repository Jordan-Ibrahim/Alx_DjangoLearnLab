from rest_framework import serializers
from django.utils import timezone
from .models import Author, Book
from datetime import date

# BookSerializer: Serializes all fields of the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Includes title, publication_year, author

    # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer: Serializes the Author model, including nested BookSerializer
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer to dynamically include all books by this author
    books = BookSerializer(many=True, read_only=True)  # from related_name='books'

    class Meta:
        model = Author
        fields = ['name', 'books']  # Includes name and nested books list
