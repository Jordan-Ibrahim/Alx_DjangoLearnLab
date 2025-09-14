from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book

@permission_required('relationship_app.can_add_book', raise_exception=True)
def create_book(request):
    return render(request, 'relationship_app/create_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'relationship_app/edit_book.html', {'book': book})


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return render(request, 'relationship_app/delete_success.html')
