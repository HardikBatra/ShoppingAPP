from django.db import models

# Create your models here.
class Contact(models.Model):
    id=models.AutoField
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    msg = models.CharField(max_length=100)
    date=models.DateField()
class Products(models.Model):
    id=models.AutoField
    heading = models.CharField(max_length=30)
    tagline = models.CharField(max_length=30)
    content = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='shop/images')
