from .models import *
from .serializers import *
from rest_framework import viewsets, permissions

#class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    permission_classes = [permissions.AllowAny]
#    serializer_class = UserSerializer
    
class FavoritesViewSet(viewsets.ModelViewSet):
    queryset = Favorites.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FavoriteSerializer
    
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CartSerializer

class ItemCartViewSet(viewsets.ModelViewSet):
    queryset = Item_cart.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ItemCartSerializer

class PurchasedBooksViewSet(viewsets.ModelViewSet):
    queryset = Purchased_books.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PurchasedBooksSerializer