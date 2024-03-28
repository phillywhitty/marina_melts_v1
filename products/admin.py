from django.contrib import admin
from .models import Product, Category, Review
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


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'review_content',
        'rate',
        'created_at',
    )



class CommentTableAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'comment',
        'created_at',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(CommentTable, CommentTableAdmin)