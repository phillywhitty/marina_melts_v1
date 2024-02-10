from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, MyWallet
from .forms import UserProfileForm, MyWalletForm

from checkout.models import Order


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
            messages.error(request, 'Update failed' +
                                    'Please ensure the form is valid.')
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


def WalletView(request):
    user = request.user
    wallet, created = MyWallet.objects.get_or_create(user=user)
    if request.method == 'POST':
        # If the form is submitted, process the form data
        form = MyWalletForm(request.POST, instance=wallet)
        if form.is_valid():
            form.save()
            return redirect('success_page')
            # Redirect to a success page after saving the form
    else:
        # If the form is not submitted, initializes the form with existing data
        form = MyWalletForm(instance=wallet)
    return render(request, 'profiles/wallet.html', {'form': form})
