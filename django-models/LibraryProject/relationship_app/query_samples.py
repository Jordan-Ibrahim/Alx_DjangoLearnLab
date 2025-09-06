from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author.

books = Author.objects.filter(name="George Orwell")

#List all books in a library.

library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()

#retrieve the librarian fo a library
library = Library.objects.get(name="Central Library")
librarian = library.librarian