from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product




def view_bag(request):
    # A view that renders the bag contents page
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):

    # Get the product object based on the item_id from the database
    product = get_object_or_404(Product, pk=item_id)
    # Extract the quantity and redirect_url from the POST request
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # Initialize size as None
    size = None

    # Check if 'product_size' is present in the POST data
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # Get the bag dictionary from the session or create an empty one
    bag = request.session.get('bag', {})

    # Check if a size is specified for the product
    if size:
        # Check if the item is already in the bag
        if item_id in list(bag.keys()):
            # Check if the specified size is already in the bag for this item
            if size in bag[item_id]['items_by_size'].keys():
                # Update the quantity for the specified size
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} \
                                {product.name} quantity to \
                                {bag[item_id]["items_by_size"][size]}')
            else:
                # Add the specified size to the bag for this item
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} \
                                            {product.name} to your bag')
        else:
            # Add a new item with the specified size to the bag
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} \
                            {product.name} to your bag')
    else:
        # Check if the item is already in the bag
        if item_id in list(bag.keys()):
            # Update the quantity for the item
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to \
                                      {bag[item_id]}')
        else:
            # Add the item to the bag with the specified quantity
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    # Update the bag in the session
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size \
                            {size.upper()} {product.name} quantity to \
                            {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size \
                            {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to \
                            {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size \
                            {size.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
