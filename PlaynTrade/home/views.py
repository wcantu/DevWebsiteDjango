from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    # Create the dummy product
    # Get the dummy product model
    main_categories = MainCategory.objects.all() #for the navbar
    sub_categories = ProductCategory.objects.all()
    one_product = Product.objects.all() #for the carousel

    # Create a dictionary of products for the carousel
    items = {}
    for index, obj in enumerate(one_product, start=1):
        key=f'item{index}'
        items[key]=obj

    page_stuff = {'carsl_itm':items,'nav_cat':main_categories, 'sub_cat':sub_categories}
    # Send the dictionary and render the page
    return render(request, 'home/homepage.html', {'items':page_stuff})
