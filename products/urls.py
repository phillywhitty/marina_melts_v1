from django.urls import path
from . import views


# Defines URL patterns for managing products app
urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('make_wishlist/', views.make_wishlist, name='make_wishlist'),
    path('leave_review/', views.leave_review, name='leave_review'),
    path('delete_review/<int:comment_id>', views.delete_review,
         name='delete_review'),
    path('editReviews/', views.editReviews, name='editReviews'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
]
