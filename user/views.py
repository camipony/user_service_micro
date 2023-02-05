from .serializers import *
from .models import *
from .serializer import *
from django.contrib.auth.models import User

from django.shortcuts import render
from rest_framework.templatetags.rest_framework import data
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class UserView(APIView):
    def get_user(self, pk):
        try:
            return User.objects.filter(username=pk)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        post = self.get_user(str(pk))
        serializer = UserSerializer(post, many=True)  
        return Response(serializer.data)    

class FavoritesView(APIView):
    def get_object(self, pk):
        try:
            return Favorites.objects.get(pk=pk)
        except Favorites.DoesNotExist:
            raise Http404
        
    def get_object_by(self, dato):
        try:
            return Favorites.objects.get(pk=dato)
        except Favorites.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        post = self.get_object_by(pk)
        serializer = FavoriteSerializer(post, many=True)  
        return Response(serializer.data)    
        
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FavoriteBookView(APIView):
    def get_object_by_book(self, dato, codigo):
        try:
            return Favorites.objects.filter(identification=dato).filter(id_book=codigo)
        except Favorites.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, codigo, format=None):
        post = self.get_object_by_book(pk, codigo)
        serializer = FavoriteSerializer(post, many=True)  
        return Response(serializer.data)    
    
class CartView(APIView):
    def get_cart(self, id):
        try:
            return Cart.objects.filter(identification = id)
        except Cart.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        post = self.get_cart(pk)
        serializer = CartSerializer(post, many=True)
        return Response(serializer.data) 

class ItemView(APIView):
    def get_cart(self, id):
        try:
            return Cart.objects.filter(identification = id)
        except Cart.DoesNotExist:
            raise Http404
        
    def post(self, request, format=None):
        dataRest = request.data
        post = self.get_cart(dataRest["id_usuario"])
        print(post[0])
        serializer = ItemCartSerializer(data = {
            "id_cart": post[0].id_cart,
            "id_book": dataRest["codigo"]
        })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ItemCartView(APIView):
        
    def get_items(self, id_cart):
        try:
            return Item_cart.objects.filter(id_cart = id_cart)
        except Item_cart.DoesNotExist:
            raise Http404
    
    def get_item(self, id):
        try:
            return Item_cart.objects.get(id_item=id)
        except Item_cart.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        post = self.get_items(pk)
        serializer = ItemCartSerializer(post, many=True)
        return Response(serializer.data) 
    
    def put(self, request, pk, format=None):
        post = self.get_items(pk)
        serializer = ItemCartSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        post = self.get_item(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ItemPay(APIView):
    def get_cart(self, id):
        try:
            return Cart.objects.filter(identification = id)
        except Cart.DoesNotExist:
            raise Http404
    
    def get_item(self, pk):
        try:
            return Item_cart.objects.filter(id_cart = pk)
        except Item_cart.DoesNotExist:
            raise Http404
    
    def add_purchase(self, data):
        try:
            serializer = PurchasedBooksSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
        except Purchased_books.DoesNotExist:
            raise Http404
    
    def delete(self, request, pk, format=None):
        cart = self.get_cart(pk)
        post = self.get_item(cart[0].id_cart)
        for i in post:
            self.add_purchase({
                "identification": pk,
                "id_book": i.id_book
            })
            i.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PurchasedView(APIView):
    def get_object_by_user(self, ident):
        try:
            return Purchased_books.objects.filter(identification = ident)
        except Purchased_books.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        post = self.get_object_by_user(pk)
        serializer = PurchasedBooksSerializer(post, many=True)
        return Response(serializer.data) 

class PurchasedBookView(APIView):
    def get_object_by_book(self, ident, codigo):
        try:
            return Purchased_books.objects.filter(identification = ident).filter(id_book=codigo)
        except Purchased_books.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, codigo, format=None):
        post = self.get_object_by_book(pk, codigo)
        serializer = PurchasedBooksSerializer(post, many=True)
        return Response(serializer.data)
