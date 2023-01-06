# Create your views here.
from django.shortcuts import render,redirect
from .models import Order
from book.models import Book
from django.contrib.auth.decorators import login_required,user_passes_test
from book.views import is_admin
from .forms import OrderForm

def is_visitor(user):
    return user.groups.filter(name='Visitor').exists()

@login_required
def get_order_list(request):
    if is_visitor(request.user):
        order_list=Order.objects.filter(user=request.user)
        return render(request,'order/user_orders.html',{'order_list':order_list})
    else:
        return render(request,'order/order_list.html',{'order_list':Order.objects.all()})

@login_required
@user_passes_test(is_visitor)
def get_create_order(request):
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            order.user=request.user
            order.save()
        return redirect('orders')
    else:
        form=OrderForm()
        return render(request,'order/create_order.html',{'form':form})

@login_required
@user_passes_test(is_admin)
def get_close_order(request,id):
    Order.delete_by_id(id)
    return redirect('orders')
