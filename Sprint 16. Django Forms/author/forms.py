from .models import Author
from django import forms

class AuthorCreationForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'surname',
                  'patronymic', 'books')
