from cgitb import lookup
from django.urls import path,include
from . import views
from order.views import OrderViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
router=DefaultRouter()
router.register(r'user', views.UserViewSet)
users_router=NestedDefaultRouter(router,r'user',lookup='user')
users_router.register(r'order',views.UsersOrderViewSet,basename='user-orders')
urlpatterns = [
    path('api/v1/',include(router.urls)),
    path('api/v1/',include(users_router.urls)),
    path('sign-up/',views.get_signup_page,name='sign-up'),
    path('login/',views.get_login_page,name='login'),
    path('',views.get_home_page,name='home'),
    path('sign-out/',views.get_signout_page,name='sign-out'),
    path('users/',views.get_users_page,name='users'),
    path('users/<int:id>',views.get_user_page,name='user-details'),
]
