from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ShoppingCartItem, ShoppingCart
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = ShoppingCart.objects.get_or_create(user=request.user)  # updated from user_id to user
    cart_item, created = ShoppingCartItem.objects.get_or_create(
        product=product, cart=cart, defaults={'qty': 1}  # updated from product_id and cart_id to product and cart
    )
    if not created:
        cart_item.qty += 1
        cart_item.save()
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart, created = ShoppingCart.objects.get_or_create(user=request.user)  # updated from user_id to user
    items = ShoppingCartItem.objects.filter(cart=cart)  # updated from cart_id to cart
    return render(request, 'cartinfo.html', {'cart': cart, 'items': items})

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(ShoppingCartItem, id=item_id, cart__user=request.user)  # updated from cart_id__user_id to cart__user
    item.delete()
    return redirect('view_cart')

@login_required
def update_cart(request, item_id):
    item = get_object_or_404(ShoppingCartItem, id=item_id, cart__user=request.user)  # updated from cart_id__user_id to cart__user
    qty = request.POST.get('qty', 1)
    if qty and int(qty) > 0:
        item.qty = int(qty)
        item.save()
    return redirect('view_cart')
