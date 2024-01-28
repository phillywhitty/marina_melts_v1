from django.contrib import admin
from .models import MyWallet


class MyWalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'card_number', 'expire_number', 'cvv_number')  

admin.site.register(MyWallet, MyWalletAdmin)