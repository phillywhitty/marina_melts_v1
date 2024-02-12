from django.contrib import admin
from .models import MyWallet, WishItem
from products.models import Product



class MyWalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'card_number', 'expire_number', 'cvv_number')


class WishItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')


admin.site.register(MyWallet, MyWalletAdmin)
admin.site.register(WishItem, WishItemAdmin)