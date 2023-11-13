from django.shortcuts import render
from .models import *

def shopping_cart(request):

    # Here you should fetch the cart items, payment methods, shipping address, etc., from your database.
    # For now, we'll assume this data is hardcoded or comes from the context.

    # cart_items = [
    #     {'name': 'Item 1', 'quantity': 1, 'price': '19.99'},
    #     {'name': 'Item 2', 'quantity': 2, 'price': '9.99'},
    #     # Add more items as needed
    # ]
    #
    # payment_methods = [
    #     {'method': 'Credit Card', 'details': '**** **** **** 1234'},
    #     # Add more methods as needed
    # ]
    #
    # shipping_address = '1234 Main St, Anytown, AN 12345'
    #
    # # Calculate subtotal, shipping, and total.
    # # These would normally be calculated based on the cart contents and user's selections.
    # subtotal = sum(float(item['price']) * item['quantity'] for item in cart_items)
    # shipping = 5.99  # Flat rate for example
    # total = subtotal + shipping
    #
    # context = {
    #     'cart_items': cart_items,
    #     'payment_methods': payment_methods,
    #     'shipping_address': shipping_address,
    #     'subtotal': '{:.2f}'.format(subtotal),
    #     'shipping': '{:.2f}'.format(shipping),
    #     'total': '{:.2f}'.format(total),
    # }
    product = Product.objects.all()  # Needs to be a shopping cart, rather than the products
    return render(request, 'cartinfo.html', {'cart':product})
