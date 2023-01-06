from django.urls import path
from .views import *
urlpatterns = [
    path('sign-up/',get_signup,name='sign-up'),
    path('login/',get_login,name='login'),
    path('',get_home,name='home'),
    path('logout/',get_logout,name='logout'),
    path('users/',get_user_list,name='users'),
    path('users/<int:id>',get_user,name='user-details'),
    
]
