from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Home page')

def faq(request):
     return render(request, 'customers/faqpage.html')
    # return HttpResponse('this works')