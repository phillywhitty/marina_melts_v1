from django.contrib import admin
from .models import Product, Category, ReviewTable
from .models import CommentTable


# Admin interface for Product model
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

# Admin interface for Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


# Admin interface for Comment model
class CommentTableAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'comment',
        'created_at',
    )

# Admin interface for Review model
class ReviewTableAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'comment',
        'created_at',
    )

# Registering models with their respective admin customizations
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CommentTable, CommentTableAdmin)
admin.site.register(ReviewTable, ReviewTableAdmin)