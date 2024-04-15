from django.urls import path
from . import views

# Defines URL patterns for managing profiles app
urlpatterns = [
    path('', views.profile, name='profile'),
    path('wallet/', views.WalletView, name='wallet'),
    path('add-wallet/', views.AddWalletView, name='add_wallet'),
    path('delete_wallet/', views.delete_wallet, name='delete_wallet'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('my_wishlist', views.my_wishlist, name="my_wishlist")
]