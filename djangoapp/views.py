from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
from utils import *

def index(request):
    return HttpResponse("Hello, this is the home page!")

def create_book(request):
    book = Book(title='Example Book', author='John Doe', year=2023)
    book.save()
    return HttpResponse('Book created successfully')