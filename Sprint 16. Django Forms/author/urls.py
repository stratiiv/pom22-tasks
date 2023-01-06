from django.urls import path
from .views import *
urlpatterns=[
    path('authors/',AuthorListView.as_view(),name='authors'),
    path('authors/<int:pk>/',AuthorDetailView.as_view(),name='author-details'),
    path('authors/create/',get_create_author,name='create-author'),
    path('authors/delete/<int:id>/',get_delete_author,name='delete-author')
]