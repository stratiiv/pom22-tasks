from django.forms import ModelForm,SelectMultiple,ModelMultipleChoiceField
from .models import Book
from author.models import Author

class AddBookForm(ModelForm):
    # authors=ModelMultipleChoiceField(queryset=Author.objects.all(),widget=SelectMultiple(),label='Select authors')
    class Meta:
        model=Book
        fields=('name','description','count')
        labels={'name':'Name','description':'Description','count':'Count'}
