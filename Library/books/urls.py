from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_list),
    path('<int:id>/', views.book_detail),
]
