# update a book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title

# expected output

'Nineteen Eighty-Four'
# Title updated successfully
