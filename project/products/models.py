from django.db import models
from datetime import datetime

# Create your models here.
# class Product
class Product(models.Model):
    x=[
        ('book','book'),
        ('computer','computer')
    ]
    name= models.CharField(max_length=30, default='ouahid')
    content = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=99.99)
    category = models.CharField(max_length=50, null=True, blank=True, choices=x)
    image= models.ImageField(upload_to='photos', default='/photos/24/10/30/automated_7909836.png')
    ative = models.BooleanField(default=True)
    created = models.DateTimeField(default=datetime.now)



