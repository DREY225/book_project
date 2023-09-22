from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenu sur le site de la bibliothèque")

def book_list(request):
    return HttpResponse("Afficher la liste des livres")

def book_add(request):
    return HttpResponse("Ajouter un livre")

def book_add(request):
    return HttpResponse("Ajouter un livre")

def book_delete(request):
    return HttpResponse("Supprimer un livre")

def book_update(request):
    return HttpResponse("mettre à jour un livre")


