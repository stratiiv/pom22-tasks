from django.urls import path
from .views import *
urlpatterns=[
    path('authors/',get_author_page,name='authors'),
    path('authors/<int:id>',get_author_details,name='author-details'),
    path('authors/create',get_create_author,name='create-author'),
    path('authors/delete/<int:id>',get_delete_author,name='delete-author')
]