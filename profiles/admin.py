from django.contrib import admin
from .models import MyWallet
from products.models import Product
from profiles.models import WishItem


class MyWalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'card_number', 'expire_number', 'cvv_number')


class WishItem(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')