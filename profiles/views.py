from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, MyWallet, WishlistTable
from .forms import UserProfileForm, MyWalletForm
from checkout.models import Order


# User Profile View


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request,
                'Update failed. Please ensure the form is valid.'
                )
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)

# Display order history for a specific order number


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


# My Wallet View


@login_required
def WalletView(request):
    checkWallet = MyWallet.objects.filter(user=request.user).first()

    context = {
        'checkWallet': checkWallet,
        'getWallet': checkWallet
    }
    return render(request, 'profiles/my_wallet_page.html', context)


# Add Wallet View


@login_required
def AddWalletView(request):
    user = request.user
    wallet, created = MyWallet.objects.get_or_create(user=user)
    if request.method == 'POST':
        form = MyWalletForm(request.POST, instance=wallet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Wallet updated successfully')
        return redirect(
            'wallet'
            )  # Redirect to avoid resubmitting POST data
    else:
        form = MyWalletForm(instance=wallet)

    context = {
        'form': form,
        'on_wallet_page': True
    }

    return render(request, 'profiles/wallet.html', context)


# Delete Wallet View


@login_required
def delete_wallet(request):
    wallet_id = request.POST.get('wallet_id')

    try:
        getWallet = MyWallet.objects.get(user=request.user, id=wallet_id)
        getWallet.delete()
    except MyWallet.DoesNotExist:
        pass

    return redirect('wallet')


# View to display the user's wishlist


@login_required
def my_wishlist(request):
    varWishlist = WishlistTable.objects.filter(user=request.user)
    context = {'varWishlist': varWishlist}
    return render(request, "profiles/wishlist.html", context)


# View to handle adding items to the user's wishlist


@login_required
def WishItem(request):
    user = request.user
    wallet, created = WishItem.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = MyWalletForm(request.POST, instance=wallet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Wallet updated successfully')
            return redirect(
                'wallet'
            )  # Redirect to avoid resubmitting POST data
    else:
        form = MyWalletForm(instance=wallet)

    context = {
        'form': form,
        'on_wallet_page': True
    }

    return render(request, 'profiles/wallet.html', context)
