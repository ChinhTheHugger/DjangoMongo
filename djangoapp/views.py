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
    # return HttpResponse('Car found:' + ", " + str(cars['_id']) + ", " + cars['carname'] + ", " + str(cars['year']) + ", " + cars['desintext'] + ", " + cars['model'] + ", " + cars['brandname'] + ", " + cars['categoryname'] + "\n")
    cl = mycol.find()
    carslist = []
    for car in cl:
        carslist.append(Car(carid=str(car['_id']),carname=car['carname'],year=car['year'],desintext=car['desintext'],model=car['model'],brandname=car['brandname'],categoryname=car['categoryname'],front=car['front']))
    context = {'carslist': carslist}
    return render(request,'list.html',context)