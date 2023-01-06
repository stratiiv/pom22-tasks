from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'order', OrderViewSet,basename="order")
urlpatterns=[
    path('api/v1/',include(router.urls)),
    path('orders/',get_orders_page,name='orders'),
    path('orders/create/',get_create_order,name='create-order'),
    path('orders/close/<int:id>/',get_close_order,name='close-order')
]