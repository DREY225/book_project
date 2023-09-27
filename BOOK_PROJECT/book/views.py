from django.shortcuts import render
from django.http import HttpResponse

from book.models import Book

def home(request):
    return HttpResponse("Bienvenu sur le site de la bibliothèque")

def book_list(request):
    
    books_list = Book.objects.all()
    
    context = {
        
        "list_books" : books_list
        
    }
    return render(request,"book/index.html",context)

def book_add(request):
    return HttpResponse("Ajouter un livre")

def book_add(request):
    return HttpResponse("Ajouter un livre")

def book_delete(request):
    return HttpResponse("Supprimer un livre")

def book_update(request):
    return HttpResponse("mettre à jour un livre")


