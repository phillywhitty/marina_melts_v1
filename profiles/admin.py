from django.contrib import admin
from .models import MyWallet


class MyWalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'default_card_number', 'default_expire_number', 'default_cvv_number')  

admin.site.register(MyWallet, MyWalletAdmin)