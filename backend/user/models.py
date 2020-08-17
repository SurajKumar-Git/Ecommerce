from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.


class User(AbstractUser):
    USERNAME_FIELD = 'username'

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)


class Address(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_addresses")
    full_name = models.CharField(max_length=32)
    address_line1 = models.CharField(max_length=128)
    address_line2 = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    postal_code = models.CharField(max_length=6, validators=[
                                   RegexValidator(r'^\d{6}$')])
    phone = models.CharField(max_length=10, validators=[
        RegexValidator(r'^\d{10}$')])

    def __str__(self):
        return f"{self.full_name}"
