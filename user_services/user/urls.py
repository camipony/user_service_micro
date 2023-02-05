from rest_framework import routers
from django.urls import path, include
from knox import views as knox_views
from .apis import *
from .views import *
from .viewSets import RegisterAPI, LoginAPI

router = routers.DefaultRouter()

#router.register('api/user', UserViewSet, 'user')
router.register('api/favorites', FavoritesViewSet, 'favorites')
router.register('api/cart', CartViewSet, 'cart')
router.register('api/itemcart', ItemCartViewSet, 'itemcart')
router.register('api/purchased', PurchasedBooksViewSet, 'bill')

#urlpatterns = router.urls

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('user/<int:pk>/', UserView.as_view()), 
    path('favorites/<int:pk>/', FavoritesView.as_view()),    
    path('cart/<int:pk>/', CartView.as_view()), 
    path('item/', ItemView.as_view()),
    path('item/<int:pk>/', ItemCartView.as_view()),
    path('favoritesbook/<int:pk>/<str:codigo>/', FavoriteBookView.as_view()),
    path('purchased/<int:pk>/', PurchasedView.as_view()),
    path('purchasedbook/<int:pk>/<str:codigo>/', PurchasedBookView.as_view()),
    path('pay/<int:pk>/', ItemPay.as_view()),
    path('', include(router.urls))
]