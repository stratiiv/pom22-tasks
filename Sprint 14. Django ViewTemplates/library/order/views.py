# Create your views here.
from django.shortcuts import render,redirect
from .models import Order
from book.models import Book
from django.contrib.auth.decorators import login_required
@login_required
def get_orders_page(request):
    if request.user.groups.all()[0].name=="Admin":
        orders=Order.objects.all()
        return render(request,'order/all_orders.html',{'orders':orders})
    else:
        orders=Order.objects.filter(user=request.user)
        return render(request,'order/user_orders.html',{'orders':orders})
@login_required
def get_create_order(request):
    if request.user.groups.all()[0].name=="Visitor":
        books=Book.objects.all()
        if request.method=='POST':
            book_name=request.POST.get('books_list')
            book=Book.objects.get(name=book_name)
            user=request.user
            Order.create(user,book)
            return redirect('orders')
        return render(request,'order/create.html',{'books':books})
    else:
        return redirect('login')

@login_required
def get_close_order(request,id):
    if request.user.groups.all()[0].name=="Admin":
        Order.delete_by_id(id)
        return redirect('orders')
    else:
        return redirect('login')