from django import forms
from .models import Book

class ExampleForm(forms.Form):
    """
    Example form for demonstration and testing.
    You can replace fields with what your project requires.
    """
    name = forms.CharField(
        max_length=100,
        required=True,
        label="Your Name",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your name"})
    )
    email = forms.EmailField(
        required=True,
        label="Email Address",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter your email"})
    )
    message = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Optional message"})
    )


class BookForm(forms.ModelForm):
    """
    A form to safely create or update Book objects.
    Demonstrates best practice — always use ModelForm to prevent SQL injection
    and validate data.
    """
    class Meta:
        model = Book
        fields = ["title", "author", "published_date"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "published_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }