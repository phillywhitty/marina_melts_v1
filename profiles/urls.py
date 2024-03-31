from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('wallet/', views.WalletView, name='wallet'),
    path('add-wallet/', views.AddWalletView, name='add_wallet'),
    path('delete_wallet/', views.delete_wallet, name='delete_wallet'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
]