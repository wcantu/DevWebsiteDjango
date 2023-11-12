from django.shortcuts import render, get_object_or_404
from .models import Product,ProductItem,ProductCategory

def product_detail(request, product_id):
    product = get_object_or_404(Product,id=product_id)
    #product_info = get_object_or_404(ProductItem,id=product_id)
   # product_info = get_object_or_404(ProductItem,product.produ)


    # Category is tricky, commented out for now. More important things to focus on
    #pCategory = get_object_or_404(ProductCategory,id=product_id)
    #res = {'product':product,'info':product_info,'category':pCategory}

    res = {'product': product}#, 'info': product_info}  # Yes, a list of dictionaries lol
    return render(request, 'productListing.html', {'item':res})