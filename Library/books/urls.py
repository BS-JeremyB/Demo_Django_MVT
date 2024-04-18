from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('create/', views.create_books, name='books_create'),
    path('list/', views.books_list, name='books_list'),
    path('<int:id>/', views.book_detail, name='books_detail'),
    path('update/<int:id>/', views.book_update, name='books_update'),
    path('delete/<int:id>/', views.book_delete, name='books_delete'),
]
