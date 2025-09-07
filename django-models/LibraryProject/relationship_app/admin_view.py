from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import UserProfile
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts   import redirect

class AdminView(DetailView):
  
  model = UserProfile
  template_name = 'relationship_app/admin_view.html'

  def get_context_data(self, **kwargs):
   
    context = super().get_context_data(**kwargs)  
    library = self.get_object()  
    context["books"] = self.object.books.all()
    return context