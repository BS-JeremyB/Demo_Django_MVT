from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('create/', views.create_books, name='books_create'),
    path('list/', views.books_list, name='books_list'),
    path('<int:id>/', views.book_detail, name='books_detail'),
]
