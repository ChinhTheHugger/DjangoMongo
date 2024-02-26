from django.db import models
from mongoengine import Document, StringField, IntField

class Book(Document):
    title = StringField(required=True)
    author = StringField(required=True)
    year = IntField(required=True)