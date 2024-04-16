from django.shortcuts import render
from django.http import HttpResponse
books = [{ 'auteur': 'Orwel', 'titre': '1984'},
        { 'auteur': 'Herbert', 'titre': 'Dune'},
        { 'auteur': 'Tolkien', 'titre': 'Le seigneur des anneaux'},
        { 'auteur': 'Doe', 'titre': 'Django pour les nuls'},
        ]
# Create your views here.
def books_list(request):
    return render(request, 'books/book_list.html', {'books': books})



def book_detail(request, id):
    return render(request, 'books/book_detail.html', {'book': books[id]})