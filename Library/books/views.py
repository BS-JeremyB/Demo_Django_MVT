from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import HelloForm, Create_books_form

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

def hello(request):
    form = HelloForm
    values = {}
    if(request.method == "POST"):
        form = HelloForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            message = form.cleaned_data['message']
            values = {'nom': nom, 'message': message}
            context = {
            'form': form,
            'values': values
            }
        return render(request, 'books/books_hello.html', context)
    

    return render(request, 'books/books_hello.html', {'form': form})

def create_books(request):

    if request.method == "POST":
        form = Create_books_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_list')

    return render(request, 'books/book_create.html', {'form' : Create_books_form})

