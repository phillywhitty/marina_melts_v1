from django.contrib import admin
from .models import Product, Category, ReviewTable
from .models import CommentTable

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )



class CommentTableAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'comment',
        'created_at',
    )
class ReviewTableAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'comment',
        'created_at',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CommentTable, CommentTableAdmin)
admin.site.register(ReviewTable, ReviewTableAdmin)