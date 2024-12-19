from django.db import models

# Create your models here.
class Female(models.Model):
    name_femal = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name_femal
    
class Male(models.Model):
    name_mal = models.CharField(max_length=50, null=True)
    girls = models.OneToOneField( Female, on_delete= models.CASCADE)
