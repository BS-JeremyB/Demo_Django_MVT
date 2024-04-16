from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def review_list(request):
    return HttpResponse("Bienvenue sur la page des critiques")