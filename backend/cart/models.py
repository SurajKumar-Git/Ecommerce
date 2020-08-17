from django.db import models
from django.contrib.auth import get_user_model

from product.models import ProductVariant
# Create your models here.


class Cart(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name="user_cart")

    def __str__(self):
        return f"{self.user}"

    def clear_cart(self):
        self.cart_items.all().delete()


class CartItemQuerySet(models.QuerySet):

    def check_in_cart(self, cart, product_variant, **kwargs):
        try:
            return self.get(cart=cart, product_variant=product_variant)
        except CartItem.DoesNotExist:
            return None


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="cart_items")
    product_variant = models.ForeignKey(
        ProductVariant, on_delete=models.CASCADE, related_name="product_variant_set")
    quantity = models.IntegerField()

    objects = models.Manager()
    cart_items = CartItemQuerySet.as_manager()
