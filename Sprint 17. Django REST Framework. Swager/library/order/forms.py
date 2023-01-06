from socket import fromshare
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=('book',)
        labels={'book':'Select book'}