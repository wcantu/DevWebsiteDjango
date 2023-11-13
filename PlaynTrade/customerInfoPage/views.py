from django.shortcuts import render

# Create your views here.
from django.shortcuts import render




def customer_info(request):
    # This will fetch all the main category objects from our model and populate the navbar with them.
    main_categories = MainCategory.objects.all()  # for the navbar

    # This will fetch all the product category objects from our model to populate the respective main cat dropdown options.
    sub_categories = ProductCategory.objects.all()

    page_stuff = {'nav_cat': main_categories, 'sub_cat': sub_categories}

    return render(request, 'info.html', {'items' : page_stuff} )###