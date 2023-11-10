from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def customer_info(request):
    # You can pass context data to use in the template here
    context = {}
    return render(request, 'customer_info_page/info.html', context)
