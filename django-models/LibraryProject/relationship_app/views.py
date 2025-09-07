from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.views import logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts   import redirect
from django.contrib.auth.decorators import permission_required


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'
def get_form(self, form_class=None):
        return UserCreationForm()

def list_books(request):
      
      books = Book.objects.all()  
      context = {'list_books': books} 
      return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
  
  model = Library
  template_name = 'relationship_app/library_detail.html'

  def get_context_data(self, **kwargs):
   
    context = super().get_context_data(**kwargs)  
    library = self.get_object()  
    context["books"] = self.object.books.all()
    return context
  
def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")

def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"

@user_passes_test(is_admin)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


def can_add_book(user):
    return user.has_perm('relationship_app.can_add_book')   
@permission_required(can_add_book)
def add_book(request):
    return render(request, 'relationship_app/add_book.html')

def can_change_book(user):
    return user.has_perm('relationship_app.can_change_book')   
@permission_required(can_change_book)
def add_book(request):
    return render(request, 'relationship_app/change_book.html')

def can_delete_book(user):
    return user.has_perm('relationship_app.can_delete_book')   
@permission_required(can_delete_book)
def delete_book(request):
    return render(request, 'relationship_app/delete_book.html') 
