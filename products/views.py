from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Review, ReviewTable
from .forms import ProductForm, ReviewForm
from django.views.decorators.csrf import csrf_exempt
from profiles.models import WishlistTable
# Product Views.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

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
                return redirect(reverse('products'))
            queries = (
                Q(name__icontains=query) | Q(description__icontains=query))
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product_id)
    all_reviews = ReviewTable.objects.filter(product=product_id)


    checkWishlist=WishlistTable.objects.filter(user=request.user, product=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.product = product
            new_review.user = request.user
            new_review.save()
            return redirect('product_detail', product_id=product_id)
    else:
        form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'all_reviews': all_reviews,
        'form': form,
        'checkWishlist':checkWishlist,
    }
    return render(request, 'products/product_detail.html', context)


@csrf_exempt
def make_wishlist(request):
    product_id = request.POST.get('product_id')
    getProduct = Product.objects.get(id=product_id)


    if WishlistTable.objects.filter(user=request.user,product=getProduct):
        WishlistTable.objects.get(user=request.user,product=getProduct).delete()
        return HttpResponse(False)
    else:
        varWishlist = WishlistTable(
            user=request.user,
            product=getProduct
        )
        varWishlist.save()
        return HttpResponse(True)


@login_required
def leave_review(request):
    if request.user.is_authenticated:
        product_id = request.POST.get('product_id')
        comment = request.POST.get('comment')
        getProduct = Product.objects.get(id=product_id)
        varReview = ReviewTable(
            user = request.user,
            product=getProduct,
            comment=comment
        )
        varReview.save()
        return redirect(f'/products/{product_id}/')
    else:
        return redirect('/accounts/login/')


@login_required
def delete_review(request, comment_id):
    if request.user.is_authenticated:
        getComment = ReviewTable.objects.get(id=comment_id)
        product_id=getComment.product.id
        getComment.delete()
        messages.success(request, "Review is deleted!")
        return redirect(f'/products/{product_id}/')
    else:
        return redirect('/accounts/login/')



@login_required
def editReviews(request):
    if request.user.is_authenticated:
        comment_content= request.POST.get('comment_content')
        commentId= request.POST.get('commentId')

        getComment = ReviewTable.objects.get(id=commentId)
        getComment.comment=comment_content
        getComment.save()
        product_id = getComment.product.id

        messages.success(request, "Review updated!")
        return redirect(f'/products/{product_id}/')
    else:
        return redirect('/accounts/login/')


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                                     Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product \
                 Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
