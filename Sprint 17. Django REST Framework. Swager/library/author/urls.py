from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'author',AuthorViewSet,basename='author')
urlpatterns=[
    path('api/v1/',include(router.urls)),
    path('authors/',get_author_page,name='authors'),
    path('authors/<int:id>/',get_author_details,name='author-details'),
    path('authors/create/',get_create_author,name='create-author'),
    path('authors/delete/<int:id>/',get_delete_author,name='delete-author')
]