"""
URL configuration for book_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home
from book.views import book_list
from book.views import book_add
from book.views import book_delete
from book.views import book_update
from author.views import author_list
from author.views import author_add
from author.views import author_delete
from author.views import author_update






urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home),
    path("add_book",book_add, name="book_add"),
    path("show_book",book_list, name="book_list"),
    path("delete_book",book_delete, name="book_delete"),
    path("update_book",book_update, name="book_update"),
    path("show_author",author_list, name="author_list"),
    path("add_author",author_add, name="author_add"),
    path("update_author",author_update, name="author_update"),
    path("delete_author",author_delete, name ="book_delete"),
        

    
  
]


