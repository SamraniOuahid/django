from django.db import models

# Create your models here.
class Female(models.Model):
    name_female = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.name_female if self.name_female else ""

class Male(models.Model):
    name_male = models.CharField(max_length=50, null=True)
    girls = models.OneToOneField(Female, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name_male if self.name_male else ""

class Login(models.Model):
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.username if self.username else ""
