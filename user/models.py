from django.db import models
from datetime import datetime


# Create your models here.
#class User(models.Model):
#    identification = models.IntegerField(primary_key=True, default=00000000)
#    name = models.CharField(max_length=100)
#    email = models.EmailField(max_length=100,unique=True)
#    date = models.DateTimeField(auto_now_add=True)
#    password = models.CharField(max_length=100)

class Favorites(models.Model):
    id_favorites = models.AutoField(primary_key=True)
    identification = models.IntegerField()
    id_book = models.CharField(max_length=100)

class Cart(models.Model):
    id_cart = models.AutoField(primary_key=True)
    identification = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)

class Item_cart(models.Model):
    id_item = models.AutoField(primary_key=True)
    id_cart = models.IntegerField()
    id_book = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)

class Purchased_books(models.Model):
    id = models.AutoField(primary_key=True)
    identification = models.IntegerField()
    id_book = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)