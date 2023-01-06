# Create your views here.
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from authentication.forms import AuthorCreationForm
from .models import Author
from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer
class AuthorViewSet(ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

def get_authors_data():
    authors = Author.objects.all()
    authors_data = []
    for author in authors:
        books_list = [book.name for book in author.books.all()]
        authors_data.append({'id': author.id, 'name': author.name, 'surname': author.surname, 'patronymic': author.patronymic,
                             'books': ''.join(books_list) if books_list else ''})
    return authors_data


@login_required
def get_author_page(request):
    if request.user.groups.all()[0].name == "Admin":
        authors_data = get_authors_data()
        return render(request, 'author/authors.html', {'authors': authors_data})
    else:
        return redirect('login')


@login_required
def get_author_details(request, id):
    if request.user.groups.all()[0].name == "Admin":
        author = Author.objects.get(pk=id)
        books_list = [book.name for book in author.books.all()]
        author_dict = {'id': author.id, 'name': author.name, 'surname': author.surname, 'patronymic': author.patronymic,
                       'books': ''.join(books_list) if books_list else ''}
        return render(request, 'author/author_details.html', {'author': author_dict})
    else:
        return redirect('login')


@login_required
def get_create_author(request):
    if request.user.groups.all()[0].name == "Admin":
        if request.method == 'POST':
            form = AuthorCreationForm(request.POST)
            try:
                Author.objects.get(name=request.POST.get('name'),surname=request.POST.get('surname'),patronymic=request.POST.get('patronymic'))
                return render(request, 'author/dublicate_author.html')
            except ObjectDoesNotExist:
                if form.is_valid():
                    form.save()
                    return redirect('authors')
        else:
            form = AuthorCreationForm()
            return render(request, 'author/create.html', {'form': form})
    else:
        return redirect('login')


@login_required
def get_delete_author(request, id):
    if request.user.groups.all()[0].name == "Admin":
        Author.delete_by_id(id)
        return redirect('authors')
    else:
        return redirect('login')
