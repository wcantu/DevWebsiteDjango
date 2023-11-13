from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    # You can add more URLs as needed
]
