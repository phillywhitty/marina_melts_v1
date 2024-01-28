from django.contrib import admin
from .models import MyWallet, WishlistItem


class MyWalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'card_number', 'expire_number', 'cvv_number')  

admin.site.register(MyWallet, MyWalletAdmin)


class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ('user','product','added_at')
    search_fields = ['product__name']
admin.site.register(WishlistItem, WishlistItemAdmin)
