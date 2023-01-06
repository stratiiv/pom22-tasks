from django.shortcuts import render

# Create your views here.
def get_user_page(request):
    return render(request,'user.html')
