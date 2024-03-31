from django.contrib import admin
from .models import MyWallet, WishlistTable


class MyWalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'card_number', 'expire_number', 'cvv_number')
admin.site.register(MyWallet, MyWalletAdmin)

class WishlistTableAdmin(admin.ModelAdmin):
    list_display=['user', 'products', 'created_at']
admin.site.register(WishlistTable)
