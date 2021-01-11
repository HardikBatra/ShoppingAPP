from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact,Products
from datetime import datetime
def index(request):
    return render(request,'shop/index.html')


def about(request):
    return render(request,'shop/about.html')

def products(request):
    products=Products.objects.all()
    params={'products':products}
    return render(request,'shop/products.html', params)

def store(request):
    return render(request,'shop/store.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        msg=request.POST.get('msg','')
        contact=Contact(name=name,email=email,msg=msg,date=datetime.now())
        contact.save()
    return render(request,'shop/contact.html')

# Create your views here.
