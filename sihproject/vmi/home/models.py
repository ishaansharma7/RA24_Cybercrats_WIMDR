from django.db import models

# Create your models here.
class CarModels(models.Model):
    car_brand_name = models.CharField(max_length=100, null='imp')
    price = models.CharField(max_length=150, default='₹10lakhs')
    mileage = models.CharField(max_length=150, default='14kmpl')
    rating_car = models.CharField(max_length=150, default='null')
    short_desc = models.TextField(null='desc')
    feat = models.TextField(null='feat')
    specs = models.TextField(null='specs')
    variants = models.TextField(null='v')
    category = models.CharField(max_length=100, null='imp')

    def __str__(self):
        return self.car_brand_name

class BrandNames(models.Model):
    brand_cap = models.CharField(max_length=100)
    brand_desc = models.TextField(null='fd')
    dealership_loc = models.TextField(null='ddd')
    
    
    def __str__(self):
        return self.brand_cap