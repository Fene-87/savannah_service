from django.db import models


# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    unit = models.CharField(max_length=10)
    price = models.DecimalField(decimal_places=2)
