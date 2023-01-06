from cgitb import lookup
from django.urls import path,include
from .views import *
from order.views import OrderViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
router=DefaultRouter()
router.register(r'user', UserViewSet)
users_router=NestedDefaultRouter(router,r'user',lookup='user')
users_router.register(r'order',UsersOrderViewSet,basename='user-orders')
urlpatterns = [
    path('api/v1/',include(router.urls)),
    path('api/v1/',include(users_router.urls)),
    path('sign-up/',get_signup_page,name='sign-up'),
    path('login/',get_login_page,name='login'),
    path('',get_home_page,name='home'),
    path('sign-out/',get_signout_page,name='sign-out'),
    path('users/',get_users_page,name='users'),
    path('users/<int:id>',get_user_page,name='user-details'),
]
