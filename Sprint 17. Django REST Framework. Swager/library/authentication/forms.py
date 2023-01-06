from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from author.models import Author


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'email', 'password1', 'password2')


class AuthorCreationForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('name', 'surname',
                  'patronymic', 'books')
