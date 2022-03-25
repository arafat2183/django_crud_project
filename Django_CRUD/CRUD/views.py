from django.shortcuts import render
from .models import BookList
from django.shortcuts import redirect
from django import forms

def index(request):

    books = BookList.objects.all()

    return render(request, 'index.html', {'books': books})

def edit(request, id):
    books = BookList.objects.get(pk=id)
    context = {
        'edit_books' : books
    }
    return render(request, 'edit.html', context)
    

def delete(request, id):
    books = BookList.objects.get(pk=id)
    books.delete()
    return redirect('/')


def add_book(request):
    return render(request, 'create.html')


def create(request):
    print(request.POST)
    title = request.GET['title']
    price = request.GET['price']
    author = request.GET['author']
    book_details = BookList(title = title, price = price, author = author)
    book_details.save()
    return redirect("/") 


def update(request, id):
    print(request.POST)
    title = request.GET['title']
    price = request.GET['price']
    author = request.GET['author']
    book_details = BookList(title = title, price = price, author = author)
    book_details.save()
    return redirect("/") 