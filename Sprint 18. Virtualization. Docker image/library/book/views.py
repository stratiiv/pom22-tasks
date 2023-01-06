# Create your views here.
from django.shortcuts import render,redirect
from .models import Book
from django.contrib.auth.decorators import login_required
from .forms import AddBookForm
from rest_framework import viewsets
from .serializers import BookSerializer
class BookViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@login_required
def get_books_page(request):        
    book_list=Book.objects.all()
    return render(request,'book/books.html',{'books':book_list})
@login_required
def get_book_details(request,id):
    book=Book.objects.get(pk=id)
    author=book.authors.all()[0]
    return render(request,'book/book_details.html',{'this_book':book,'this_book_author':author})

@login_required
def get_filtered_books(request):
    name=request.GET.get('name')
    author_full=request.GET.get('authors_list')
    if name!='':
        return render(request,'book/books.html',{'books':Book.objects.filter(name=name)})
    elif author_full!='Choose author':
        books=[]
        for book in Book.objects.all():
            for author in book.authors.all():
                if author.name +' '+ author.patronymic +' '+ author.surname == author_full:
                    books.append(book)
    return render(request,'book/filtered.html',{'books':books})     
@login_required
def get_add_book(request):
    if request.user.groups.all()[0].name == "Admin":
        if request.method=='POST':
            form=AddBookForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('books')
        else:
            form=AddBookForm()
            return render(request,'book/add.html',{'form':form})
    else:
        return redirect('login')

    