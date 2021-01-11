from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'shop/index.html')


def about(request):
    return render(request,'shop/about.html')

def products(request):
    return render(request,'shop/products.html')

def store(request):
    return render(request,'shop/store.html')

def contact(request):
    return render(request,'shop/contact.html')

# Create your views here.
