from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import UserProfile

class MemberView(DetailView):
    
    model = UserProfile
    template_name = 'relationship_app/member_view.html'
    
    def get_context_data(self, **kwargs):
     
        context = super().get_context_data(**kwargs)  
        library = self.get_object()  
        context["books"] = self.object.books.all()
        return context