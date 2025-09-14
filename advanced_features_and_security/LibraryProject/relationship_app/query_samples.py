from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author.
author_name = "George Orwells"
author = Author.objects.get(name=author_name)
books = Author.objects.filter(author=author)

#List all books in a library.
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

#retrieve the librarian fo a library
librarian = Librarian.objects.get(library="Central Library")
librarian_name = librarian.name