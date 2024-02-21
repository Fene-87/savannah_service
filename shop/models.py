import random
import string

from django.db import models


def generate_random_code():
    length = 6
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


# Create your models here.
class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    customer_code = random_id = models.CharField(max_length=6, unique=True, default=generate_random_code)


class Item(models.Model):
    item = models.CharField(max_length=100)
    unit = models.CharField(max_length=10)
    price = models.DecimalField(decimal_places=2)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, on_update=models.PROTECT, related_name='orders')
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, on_update=models.PROTECT)
    amount = models.DecimalField(decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)
