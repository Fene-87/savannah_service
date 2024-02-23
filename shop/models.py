import logging

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import africastalking

from shop.utils import generate_random_code


sms = africastalking.SMS


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    customer_code = models.CharField(max_length=6, unique=True, default=generate_random_code)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'customer_code']

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'customers'


class Item(models.Model):
    item = models.CharField(max_length=100)
    unit = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='orders')
    items = models.ManyToManyField(Item, related_name='orders')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

        self.send_sms()

    def send_sms(self):
        username = 'sandbox'
        api_key = '8a98028e205ac56d5ba81d1aa2b7caa1a6ce85e5f516c0924abffccb3ec1ebc0'
        logging.info(f"Username: {username}, API Key: {api_key}")

        africastalking.initialize(username, api_key)
        africastalking_sms = africastalking.SMS

        # Customize the SMS message
        message = f"Thank you for your order! Order ID: {self.id}"

        phone_number = ["+254713129863"]

        try:
            response = africastalking_sms.send(message, phone_number)
            print(response)
        except Exception as e:
            print(f"SMS sending failed: {str(e)}")

