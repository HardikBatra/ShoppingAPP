from django.contrib import admin

# Register your models here.
from .models import Contact,Products
admin.site.register(Contact)
admin.site.register(Products)