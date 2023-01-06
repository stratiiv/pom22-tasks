from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'book', views.BookViewSet,basename="book")
urlpatterns=[
    path('api/v1/',include(router.urls)),
    path('books/',views.get_books_page,name='books'),
    path('books/<int:id>/',views.get_book_details,name='book-details'),
    path('books/filter/',views.get_filtered_books,name='filter-books'),
    path('books/add/',views.get_add_book,name='add-book')
]