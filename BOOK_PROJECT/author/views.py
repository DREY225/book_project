from django.shortcuts import render
from django.http import HttpResponse
from author.models import Author


def home(request):
    return HttpResponse("Bienvenu sur le site de la bibliothèque")

def author_list(request):
    
    authors_list = Author.objects.all()
    
    context = {
        
        "list_authors" : authors_list
        
    }
    return render(request,"author/index.html",context)



def author_add(request):
    return HttpResponse("Ajouter un autheur")

def author_add(request):
    return HttpResponse("Ajouter un autheur")

def author_delete(request):
    return HttpResponse("Supprimer un autheur")

def author_update(request):
    return HttpResponse("mettre à jour un autheur")