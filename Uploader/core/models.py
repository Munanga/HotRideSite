from django.db import models
from djmoney.models.fields import MoneyField
from django.urls import reverse


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=120)
    brand = models.CharField(max_length=120)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    year = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='ride_profile_pics/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:home')

class Manufacturer(models.Model):
    name = models.CharField(max_length=120)
    networth = models.PositiveIntegerField(default=0)
    stockprice = models.PositiveSmallIntegerField(default=0)
    car = models.OneToOneField(Car,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


