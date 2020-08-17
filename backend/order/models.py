from django.db import models

from django.contrib.auth import get_user_model

from product.models import ProductVariant
from user.models import Address
# Create your models here.


class Order(models.Model):

    statues = [("C", "Canceled"), ("P", "Order Placed"),
               ("S", "Shipped"), ("D", "Delivered")]
    user = models.ForeignKey(
        get_user_model(), on_delete=models.DO_NOTHING, related_name="UserOrders")
    shipping_address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=statues, default="P")
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        ordering = ("-created", "-id")


class OrderItem(models.Model):

    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items")
    product_variant = models.ForeignKey(
        ProductVariant, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.order} - {self.product_variant}"
