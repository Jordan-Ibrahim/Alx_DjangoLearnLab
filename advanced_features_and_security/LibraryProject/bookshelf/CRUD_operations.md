from bookshelf.models import Book

# Create a book
book = Book.objects.create(
   title="1984",
   author="George Orwell",
   publication_year=1949
)
book


# Expected output (example, actual ID may differ):
# <Book: 1984 by George Orwell (1949)>

# retrieve a book

book = Book.objects.get(title="1984")
book.title, 
book.author, 
book.publication_year

# expected output

('1984', 'George Orwell', 1949)
# Retrieved book details successfully

# update a book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title

# expected output

'Nineteen Eighty-Four'
# Title updated successfully

from bookshelf.models import Book"
# delete a book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()

# expected output

(1, {'book_store.Book': 1})
<QuerySet []>
# Book deleted successfully, database is empty


