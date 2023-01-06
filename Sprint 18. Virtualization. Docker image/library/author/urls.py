from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'author',views.AuthorViewSet,basename='author')
urlpatterns=[
    path('api/v1/',include(router.urls)),
    path('authors/',views.get_author_page,name='authors'),
    path('authors/<int:id>/',views.get_author_details,name='author-details'),
    path('authors/create/',views.get_create_author,name='create-author'),
    path('authors/delete/<int:id>/',views.get_delete_author,name='delete-author')
]