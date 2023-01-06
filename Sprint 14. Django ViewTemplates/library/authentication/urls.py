from django.urls import path
from .views import *
urlpatterns = [
    path('sign-up/',get_signup_page,name='sign-up'),
    path('login/',get_login_page,name='login'),
    path('',get_home_page,name='home'),
    path('sign-out/',get_signout_page,name='sign-out'),
    path('users/',get_users_page,name='users'),
    path('users/<int:id>',get_user_page,name='user-details'),
]
