# Create your views here.
from django.shortcuts import render,redirect
from .models import Book
from django.contrib.auth.decorators import login_required,user_passes_test
from .forms import AddBookForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

@login_required
def get_book_list(request):
    queryset=Book.objects.all()
    return render(request,'book/book_list.html',{'book_list':queryset,'all_books':queryset})

@login_required
def get_filtered_books(request):
    name=request.GET.get('name')
    author_full=request.GET.get('authors_list')
    book_list=[]
    if not name and author_full=='Choose author':
        return redirect('books')
    elif name!='':
        return render(request,'book/book_list.html',{'book_list':Book.objects.filter(name=name),'all_books':Book.objects.all()})
    elif author_full!='Choose author':
        for book in Book.objects.all():
            for author in book.authors.all():
                if str(author) == author_full:
                    book_list.append(book)
    return render(request,'book/book_list.html',{'book_list':book_list,'all_books':Book.objects.all()})     

@login_required
@user_passes_test(is_admin)
def get_add_book(request):
    if request.method=='POST':
        form=AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')   
    else:
        form=AddBookForm()
    return render(request,'book/add_book.html',{'form':form})


class BookDetailView(LoginRequiredMixin,generic.DetailView):
    model=Book
    context_object_name = 'book'