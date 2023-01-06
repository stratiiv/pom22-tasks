# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from book.views import is_admin
from authentication.forms import UserRegisterForm
from order.models import Order

def get_home(request):
    return render(request, 'home.html')


def get_signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        admin = request.POST.get('as_admin')
        if form.is_valid():
            form.save()
            user = User.objects.get(username=form.cleaned_data['username'])
            if admin != None:
                admin_group,created = Group.objects.get_or_create(name='Admin')
                admin_group.user_set.add(user)
            else:
                members_group,created = Group.objects.get_or_create(name='Visitor')
                members_group.user_set.add(user)
        return redirect('login')
    else:
        form = UserRegisterForm()
        return render(request, 'authentication/signup.html', {'form': form})


def get_login(request):
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


def get_logout(request):
    logout(request)
    return redirect('home')


@login_required
@user_passes_test(is_admin)
def get_user_list(request):
    user_list = User.objects.exclude(username='su').order_by('id')
    return render(request, 'authentication/user_list.html', {'user_list': user_list})

@login_required
@user_passes_test(is_admin)
def get_user(request, id):
    user = get_object_or_404(User,pk=id)
    group = list(user.groups.all())
    orders = ''
    for order in Order.objects.all():
        if order.user == user:
            orders += str(order.id)+' '
    return render(request, 'authentication/user_details.html', {'this_user': user, 'group': group[0], 'orders': orders})

