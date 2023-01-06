from django.urls import path
from .views import *
urlpatterns=[
    path('orders',get_orders_page,name='orders'),
    path('orders/create',get_create_order,name='create-order'),
    path('orders/close/<int:id>',get_close_order,name='close-order')
]