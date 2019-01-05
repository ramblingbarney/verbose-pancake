from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages


def view_cart(request):
    """
    A view that renders the cart contents page
    """
    cart = request.session.get('cart', {})

    if len(cart) > 0:

        return render(request, "cart.html")
    else:
        return redirect(reverse('products'))

def add_to_cart(request, id):
    """
    Add a quantity of the specified product to the cart
    """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if id in cart:
        cart[id] += quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    messages.add_message(request, messages.SUCCESS, 'Added to cart')
    system_messages = messages.get_messages(request)
    return redirect(reverse('products'))

def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified amount
    """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
