from django.urls import path,include
from . import views

urlpatterns = [

    path('', views.home),
    # path('Trading Cards/<str:product_cat>', views.navigationLink, name = 'product_cat'),
    path('<str:dynamic_value>/', views.navigationLink, name='dynamic_product_category'),

]

