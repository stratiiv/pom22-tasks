# Create your views here.
from django.shortcuts import render,redirect
from .models import Book
from django.contrib.auth.decorators import login_required
@login_required
def get_books_page(request):
    if request.method=='POST':
        name=request.POST.get('name')
        author_full=request.POST.get('authors_list')
        if name!='':
            return render(request,'book/books.html',{'books':Book.objects.filter(name=name)})
        elif author_full!='Choose author':
            books=[]
            for book in Book.objects.all():
                for author in book.authors.all():
                    if author.name +' '+ author.patronymic +' '+ author.surname == author_full:
                        books.append(book)
            return render(request,'book/books.html',{'books':books})
                    
    book_list=Book.objects.all()
    return render(request,'book/books.html',{'books':book_list})
@login_required
def get_book_details(request,id):
    book=Book.objects.get(pk=id)
    author=book.authors.all()[0]
    return render(request,'book/book_details.html',{'this_book':book,'this_book_author':author})
