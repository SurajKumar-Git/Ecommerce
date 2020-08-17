from django.db import models
from colorfield.fields import ColorField

# Create your models here.


class Color(models.Model):
    name = models.CharField(max_length=16)
    code = ColorField(default="#FF0000")

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=8)
    length = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.length}"

    class Meta:
        ordering = ["length"]


class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=16)
    description = models.CharField(max_length=64)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="products")

    def __str__(self):
        return self.name

    def get_first_color(self):
        return self.product_variants.first().color


class ProductVariant(models.Model):

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_variants")
    color = models.ForeignKey(
        Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.PROTECT)

    class Meta:
        ordering = ["product", "color", "size"]

    def __str__(self):
        return f"{self.product} {self.color} {self.size}"


class ProductInventoryQuerySet(models.QuerySet):

    def check_stock(self, variant, quantity):
        inventory = self.get(variant=variant)
        return (quantity <= inventory.stock, inventory.stock)

    def update_stock(self, variant, quantity):
        inventory = self.get(variant=variant)
        if (inventory.stock - quantity) >= 0:
            inventory.stock -= quantity
        inventory.save()


class ProductInventory(models.Model):

    variant = models.OneToOneField(
        ProductVariant, on_delete=models.CASCADE, related_name="product_inventory")
    stock = models.IntegerField()
    price = models.IntegerField()

    objects = models.Manager()
    inventory = ProductInventoryQuerySet.as_manager()

    def __str__(self):
        return f"{self.variant} {self.stock} {self.price}"

    def update_stock(self, quantity):
        self.stock += quantity
        self.save()


class ProductImageQuerySet(models.QuerySet):

    def get_image(self, color, product):
        return self.filter(color=color, product=product).first().image


class ProductImage(models.Model):

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_images")
    color = models.ForeignKey(
        Color, on_delete=models.CASCADE)
    image = models.ImageField()

    objects = models.Manager()
    productimages = ProductImageQuerySet.as_manager()

    class Meta:
        ordering = ["product", "color"]

    def __str__(self):
        return f"{self.color} - {self.image}"
