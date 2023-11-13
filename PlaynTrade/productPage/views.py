from django.shortcuts import render, get_object_or_404
from .models import *

def product_detail(request, product_id):
    # Create the dummy product
    # Get the dummy product model
    main_categories = MainCategory.objects.all()  # for the navbar
    sub_categories = ProductCategory.objects.all()

    product = get_object_or_404(Product,id=product_id)


    res = {'product': product, 'nav_cat': main_categories, 'sub_cat': sub_categories}
    return render(request, 'productListing.html', {'items':res})