from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'order', views.OrderViewSet,basename="order")
urlpatterns=[
    path('api/v1/',include(router.urls)),
    path('orders/',views.get_orders_page,name='orders'),
    path('orders/create/',views.get_create_order,name='create-order'),
    path('orders/close/<int:id>/',views.get_close_order,name='close-order')
]