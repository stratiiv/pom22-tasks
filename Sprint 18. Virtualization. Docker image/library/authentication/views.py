# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from authentication.forms import UserRegisterForm
from order.models import Order
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from order.views import OrderViewSet
class UserViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
class UsersOrderViewSet(OrderViewSet):
    def get_queryset(self):
        return Order.objects.filter(user=self.kwargs['user_pk'])

def get_home_page(request):
    return render(request, 'home.html')

def get_signup_page(request):

    admin_group = Group.objects.get(name='Admin')
    members_group = Group.objects.get(name='Visitor')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        admin = request.POST.get('as_admin')

        if form.is_valid():
            form.save()

            user = User.objects.get(username=form.cleaned_data['username'])

            if admin != None:
                admin_group.user_set.add(user)
            else:
                members_group.user_set.add(user)

            return redirect('login')
    else:
        form = UserRegisterForm()
        return render(request, 'authentication/signup.html', {'form': form})


def get_login_page(request):

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'authentication/login_fail.html')
    else:
        form = AuthenticationForm()
        return render(request, 'authentication/login.html', {'form': form})


def get_signout_page(request):
    logout(request)
    return redirect('home')


@login_required
def get_users_page(request):
    if request.user.groups.all()[0].name == "Admin":
        users_list = User.objects.exclude(username='su').order_by('id')
        return render(request, 'authentication/users.html', {'users': users_list})
    else:
        return redirect('login')


@login_required
def get_user_page(request, id):
    if request.user.groups.all()[0].name == "Admin":
        user = User.objects.get(pk=id)
        group = list(user.groups.all())
        orders = ''
        for order in Order.objects.all():
            if order.user == user:
                orders += str(order.id)+' '
        return render(request, 'authentication/user_details.html', {'this_user': user, 'group': group[0], 'orders': orders})
    else:
        return redirect('login')
