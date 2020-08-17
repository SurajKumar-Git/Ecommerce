from django.db.models.signals import post_save
from django.dispatch import receiver
from order.models import Order


@receiver(post_save, sender=Order)
def update_product_stock(sender, instance, created, **kwargs):
    if not created and instance.status == "C":
        for order_item in instance.order_items.all():
            product_variant = order_item.product_variant
            quantity = order_item.quantity
            product_variant.product_inventory.update_stock(quantity)
