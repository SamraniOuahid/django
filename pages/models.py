from django.db import models

# Create your models here.
#  on to on
class Female(models.Model):
    name_female = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.name_female
class Male(models.Model):
    name_male = models.CharField(max_length=20, null=True)
    girls = models.OneToOneField(Female, on_delete=models.CASCADE)
    def __str__(self):
        return self.name_male
    
# on to more


class Product(models.Model):
    title = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=20, null=True)
    products = models.ManyToManyField(Product, null= True)
    def __str__(self):
        return self.name