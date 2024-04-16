from django.shortcuts import render, redirect
from django.urls import reverse  # Added import for reverse
from django.http import HttpResponse  # Added import for HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, ReviewTable
from .forms import ProductForm
from django.views.decorators.csrf import csrf_exempt
from profiles.models import WishlistTable


# View to display all products with search, sort, and filter functionalities
def all_products(request):
    """A view to show all products, including sorting and search queries"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search basis!")
                return redirect(reverse('all_products'))
                queries = (
                            Q(name__icontains=query) |
                            Q(description__icontains=query)
                        )
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


# View to display product details and related reviews
def product_detail(request, product_id):
    """A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)
    all_reviews = ReviewTable.objects.filter(product=product_id)
    check_wishlist = WishlistTable.objects.filter(
                                                    user=request.user,
                                                    product=product_id
                                                )

    context = {
        'product': product,
        'all_reviews': all_reviews,
        'check_wishlist': check_wishlist,
    }
    return render(request, 'products/product_detail.html', context)


# Add Review View
@login_required
def leave_review(request):
    if request.user.is_authenticated:
        product_id = request.POST.get('product_id')
        comment = request.POST.get('comment')
        getProduct = Product.objects.get(id=product_id)
        varReview = ReviewTable(
            user=request.user,
            product=getProduct,
            comment=comment
        )
        varReview.save()
        return redirect('product_detail', product_id=product_id)
    else:
        return redirect('login')


# Edit Review View
@login_required
def edit_reviews(request):
    if request.user.is_authenticated:
        comment_content = request.POST.get('comment_content')
        comment_id = request.POST.get('commentId')

        get_comment = ReviewTable.objects.get(id=comment_id)
        get_comment.comment = comment_content
        get_comment.save()
        product_id = get_comment.product.id

        messages.success(request, "Review updated!")
        return redirect('product_detail', product_id=product_id)
    else:
        return redirect('login')


# Delete Review View
@login_required
def delete_review(request, comment_id):
    if request.user.is_authenticated:
        get_comment = ReviewTable.objects.get(id=comment_id)
        product_id = get_comment.product.id
        get_comment.delete()
        messages.success(request, "Review is deleted!")
        return redirect('product_detail', product_id=product_id)
    else:
        return redirect('login')


# View to display product wishlist items
@csrf_exempt
def make_wishlist(request):
    product_id = request.POST.get('product_id')
    getProduct = Product.objects.get(id=product_id)

    if WishlistTable.objects.filter(
        user=request.user,
        product=getProduct
         ).exists():
        WishlistTable.objects.get(
            user=request.user,
            product=getProduct
            ).delete()
        return HttpResponse(False)
    else:
        var_wishlist = WishlistTable(
            user=request.user,
            product=getProduct
        )
        var_wishlist.save()
        return HttpResponse(True)
