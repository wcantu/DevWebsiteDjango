from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    # Create the dummy product
    # Get the dummy product model
    one_product = Product.objects.first()


    return render(request, 'home/homepage.html', {'test_product':one_product})
