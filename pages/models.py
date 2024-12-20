from django.db import models

# Create your models here.
# One-to-One Relationship
class Female(models.Model):
    name_female = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name_female

class Male(models.Model):
    name = models.CharField(max_length=20, null=True)
    age = models.IntegerField(null=True)
    enfant = models.IntegerField(null=True)
    image = models.ImageField(upload_to='photos/%y/%m/%d', null=True, blank=True)
    girls = models.OneToOneField(Female, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Many-to-Many Relationship
class Product(models.Model):
    title = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=20, null=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name
