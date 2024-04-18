from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import HelloForm, Create_books_form
from .models import *

# Create your views here.
def books_list(request):
    books_from_db = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books_from_db})
   



def book_detail(request, id):
    # try:
        book_from_db = Book.objects.get(id=id)
        return render(request, 'books/book_detail.html', {'book_in_template': book_from_db})
    # except Exception as e:
    #     return redirect('books_list')
    

def book_update(request, id):
    book_from_db = Book.objects.get(id=id)
    #POST
    if request.method == 'POST':
        form = Create_books_form(request.POST, instance=book_from_db)
        if form.is_valid():
            form.save()
            return redirect('books_list')
    #GET
    form_from_view = Create_books_form(instance= book_from_db)
    return render(request, 'books/book_update.html', {'form_in_template' : form_from_view} )


def book_delete (request, id):
    book_from_db = Book.objects.get(id=id)
    book_from_db.delete()
    return redirect('books_list')
    






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

