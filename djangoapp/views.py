from django.http import HttpResponse
from django.shortcuts import render
from .models import Car
from utils import *

def index(request):
    return HttpResponse("Hello, this is the home page!")

# def create_book(request):
#     # book = Book(title='Example Book', author='John Doe', year=2023)
#     book = {"title": "Example Book", "author": "John Doe", "year": "2023"}
#     mycol.insert_one(book)
#     return HttpResponse('Book created successfully')

def list_cars(request):
    # cars = mycol.find_one()
    # return HttpResponse('Car found:' + ", " + cars['carname'] + ", " + str(cars['year']) + ", " + cars['desintext'] + ", " + cars['model'] + ", " + cars['brandname'] + ", " + cars['categoryname'])
    cl = mycol.find()
    carslist = []
    for car in cl:
        carslist.append(Car(car['carname'],car['year'],car['desintext'],car['model'],car['brandname'],car['categoryname']))
    context = {'carslist': carslist}
    return render(request,'list.html',context)