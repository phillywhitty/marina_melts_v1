from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

    # Initialize variables
    bag_items = []
    total = 0
    product_count = 0

    # Retrieve bag from session or create an empty bag
    bag = request.session.get('bag', {})

    # Iterate through items in the bag
    for item_id, item_data in bag.items():
        # Check if item_data is a quantity (int) or a dictionary with sizes
        if isinstance(item_data, int):
            # Get product associated with the item_id
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            # Add item details to bag_items list
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)

            # Iterate through sizes and quantities in item_data
            for size, quantity in item_data['items_by_size'].items():
                # Calculate total cost and product count for each item size
                total += quantity * product.price
                product_count += quantity
                # Add item details to bag_items list including size
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    # Calculate delivery cost and check for free delivery eligibility
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    # Calculate grand total including delivery cost
    grand_total = delivery + total
    
    # Prepare context dictionary with relevant data
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    # Return context dictionary for rendering the template
    return context