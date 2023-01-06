from django.shortcuts import render

# Create your views here.
def get_book_page(request):
    return render(request,'book.html')