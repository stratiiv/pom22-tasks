# Create your views here.
from django.shortcuts import render,redirect
from .models import Order
from book.models import Book
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from rest_framework.viewsets import ModelViewSet
from .serializers import OrderSerializer
class OrderViewSet(ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    
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
        if request.method=='POST':
            form=OrderForm(request.POST)
            if form.is_valid():
                order=form.save(commit=False)
                order.user=request.user
                order.save()
            else:
                print(form.errors)
            return redirect('orders')
        else:
            form=OrderForm()
            return render(request,'order/create.html',{'form':form})
    else:
        return redirect('login')

@login_required
def get_close_order(request,id):
    if request.user.groups.all()[0].name=="Admin":
        Order.delete_by_id(id)
        return redirect('orders')
    else:
        return redirect('login')