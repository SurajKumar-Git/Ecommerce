from django.contrib import admin
from .models import Color, Size, Category, Product, ProductVariant, ProductImage, ProductInventory
# Register your models here.


class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ["product", "color", "size"]


admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductVariant, ProductVariantAdmin)
admin.site.register(ProductInventory)
admin.site.register(ProductImage)
