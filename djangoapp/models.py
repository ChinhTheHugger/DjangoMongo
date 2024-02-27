from django.db import models
from mongoengine import Document, StringField, IntField

# class Book(Document):
#     title = StringField(required=True)
#     author = StringField(required=True)
#     year = IntField(required=True)

class Car(models.Model):
    carname = models.CharField(max_length=50,null=True)
    year = models.IntegerField(default=0)
    desintext = models.CharField(max_length=50,null=True)
    model = models.CharField(max_length=50,null=True)
    brandname = models.CharField(max_length=50,null=True)
    categoryname = models.CharField(max_length=50,null=True)
    
    