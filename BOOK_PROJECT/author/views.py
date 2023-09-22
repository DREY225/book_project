from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenu sur le site de la bibliothèque")

def author_list(request):
    return HttpResponse("Afficher la liste des livres")

def author_add(request):
    return HttpResponse("Ajouter un autheur")

def author_add(request):
    return HttpResponse("Ajouter un autheur")

def author_delete(request):
    return HttpResponse("Supprimer un autheur")

def author_update(request):
    return HttpResponse("mettre à jour un autheur")