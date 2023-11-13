from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ShoppingCartItem, ShoppingCart
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = ShoppingCart.objects.get_or_create(user_id=request.user)
    cart_item, created = ShoppingCartItem.objects.get_or_create(
        product_id=product, cart_id=cart, defaults={'qty': 1}
    )
    if not created:
        cart_item.qty += 1
        cart_item.save()
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart, created = ShoppingCart.objects.get_or_create(user_id=request.user)
    items = ShoppingCartItem.objects.filter(cart_id=cart)
    return render(request, 'cartinfo.html', {'cart': cart, 'items': items})

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(ShoppingCartItem, id=item_id, cart_id__user_id=request.user)
    item.delete()
    return redirect('view_cart')

@login_required
def update_cart(request, item_id):
    item = get_object_or_404(ShoppingCartItem, id=item_id, cart_id__user_id=request.user)
    qty = request.POST.get('qty', 1)
    if qty:
        item.qty = int(qty)
        item.save()
    return redirect('view_cart')
