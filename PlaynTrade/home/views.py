from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from .models import ProductCategory, Product
# Create your views here.

def home(request):


    # This will fetch all the main category objects from our model and populate the navbar with them.
    main_categories = MainCategory.objects.all() #for the navbar

    # This will fetch all the product category objects from our model to populate the respective main cat dropdown options.
    sub_categories = ProductCategory.objects.all()




    one_product = Product.objects.all() #for the carousel

    # This fetches all created products from our model.
    # This needs to be changed to fetch 3 items. Because the carousel will only display 3 items in the html.
    items = {}
    for index, obj in enumerate(one_product, start=1):
        key=f'item{index}'
        items[key]=obj

    page_stuff = {'carsl_itm':items,'nav_cat':main_categories, 'sub_cat':sub_categories}


    # Send the dictionary and render the page
    return render(request, 'home/homepage.html', {'items':page_stuff})

# This will be the view function for rendering the .html for the navigation links
def navigationLink(request, dynamic_value):
    temp_product_category = get_object_or_404(ProductCategory, category_name=dynamic_value)



    #query all the products in the sub
    products_for_category = Product.objects.filter(category_id=temp_product_category)

    #populate dict with products
    temp_dict = {}
    for index,product in enumerate(products_for_category):
        key = f'item{index}'
        temp_dict[key] = product

    result = {'product_cat':temp_product_category , 'items':temp_dict }



    return render(request, 'home/testing.html', {'info':result} )
    # return HttpResponse('The nav link works!')


# second, get ALL the items in that main category&sub category combo
# third, pass as context to testing.html
# fourht, loop through the context and populate the page with cards.
# NOTE: Seems like we need to modify the top_navbar.html so that they can route to a url that this view function will use
