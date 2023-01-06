from django import forms
from .models import Book
from author.models import Author

class AddBookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=('name','description','count')
        labels={'name':'Name','description':'Description','count':'Count'}
