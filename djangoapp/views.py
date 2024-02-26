from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
from utils import *

def index(request):
    return HttpResponse("Hello, this is the home page!")

def create_book(request):
    # book = Book(title='Example Book', author='John Doe', year=2023)
    book = {"title": "Example Book", "author": "John Doe", "year": "2023"}
    mycol.insert_one(book)
    return HttpResponse('Book created successfully')

def find_book(request):
    book = mycol.find_one()
    print(book)
    return HttpResponse('Book found: ' + book['title'] + ", " + book['author'] + ", " + book['year'])