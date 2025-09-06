from bookshelf.models import Book"

# delete a book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()

# expected output

(1, {'book_store.Book': 1})
<QuerySet []>
# Book deleted successfully, database is empty