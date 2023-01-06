# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from order.models import Order

def get_home_page(request):
    return render(request,'home.html')
def get_signup_page(request):
    admin_group=Group.objects.get(name='Admin')
    members_group=Group.objects.get(name='Visitor')
    if request.method=='POST':
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        admin=request.POST.get('as_admin')
        user=User.objects.create_user(username=email,first_name=first_name,last_name=last_name,email=email,password=password) 
        if admin!=None:
            admin_group.user_set.add(user)
        else:
            members_group.user_set.add(user)
        return redirect('login')  
    return render(request,'authentication/signup.html')

def get_login_page(request):
    if request.method=='POST':
        email=request.POST.get("email")
        password=request.POST.get("password")
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'authentication/login_fail.html')
    return render(request,'authentication/login.html')

def get_signout_page(request):
    logout(request)
    return redirect('home')

@login_required
def get_users_page(request):
    if request.user.groups.all()[0].name=="Admin":
        users_list=User.objects.exclude(username='su').order_by('id')
        return render(request,'authentication/users.html',{'users':users_list})
    else:
        return redirect('login')

@login_required
def get_user_page(request,id):
    if request.user.groups.all()[0].name=="Admin":
        user=User.objects.get(pk=id)
        group=list(user.groups.all())
        orders=''
        for order in Order.objects.all():
            if order.user==user:
                orders+=str(order.id)+' '
        return render(request,'authentication/user_details.html',{'this_user':user,'group':group[0],'orders':orders})
    else:
        return redirect('login')