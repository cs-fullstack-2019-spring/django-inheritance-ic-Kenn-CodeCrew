from django.db import models

# Create your models here.
class CarModel(models.Model):
    year = models.IntegerField(default=0)
    make = models.CharField(max_length=100, default="")
    model = models.CharField(max_length=100, default="")
