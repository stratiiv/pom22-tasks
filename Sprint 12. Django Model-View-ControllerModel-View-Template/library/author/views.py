from django.shortcuts import render

# Create your views here.
def get_author_page(request):
    return render(request,'author.html')
