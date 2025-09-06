from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author.

books = Author.objects.filter(author_name="George Orwell")

#List all books in a library.

library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

#retrieve the librarian fo a library
library = Library.objects.get(name="Central Library")
librarian = library.librarian