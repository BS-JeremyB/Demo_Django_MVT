from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenue dans ma bibliothèque")