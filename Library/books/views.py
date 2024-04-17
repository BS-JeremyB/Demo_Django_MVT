from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import HelloForm, Create_books_form
from .models import *

# Create your views here.
def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})



def book_detail(request, id):
    try:
        book = Book.objects.get(id=id)
        return render(request, 'books/book_detail.html', {'book': book})
    except Exception as e:
        return HttpResponse("Le livre n'existe pas, erreur : ",e)

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

