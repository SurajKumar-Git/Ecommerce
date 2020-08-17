from rest_framework import serializers
from .models import Color, Size, Product, ProductImage, Category, ProductVariant, ProductInventory


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ["id", "name", "code"]


class SizeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = ["id", "name", "length"]


class CategorySerilazers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]


class ProductVariantCreateUpdateSerializers(serializers.ModelSerializer):
    color = serializers.PrimaryKeyRelatedField(queryset=Color.objects.all())
    size = serializers.PrimaryKeyRelatedField(queryset=Size.objects.all())

    class Meta:
        model = ProductVariant
        fields = ["product", "color", "size", ]


class ProductVariantSerializers(serializers.ModelSerializer):

    color = ColorSerializer(read_only=True)
    size = SizeSerializers(read_only=True)

    product_inventory = serializers.HyperlinkedRelatedField(
        view_name="productinventory-detail", read_only=True)

    class Meta:
        model = ProductVariant
        fields = ["id", "color", "size", "product_inventory"]


class ProductInventorySerializers(serializers.ModelSerializer):

    class Meta:
        model = ProductInventory
        fields = ["stock", "price"]


class ProductImageSerializers(serializers.ModelSerializer):

    image = serializers.CharField(source="image.url")

    class Meta:
        model = ProductImage
        fields = ["color", "image"]


class ProductSerializers(serializers.ModelSerializer):

    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ["id", "name", "description", "category"]


class ProductListSerializers(ProductSerializers):

    images = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        return obj.product_variants.first().product_inventory.price

    def get_images(self, obj):
        images = [productimage.image.url for productimage in obj.product_images.filter(
            color=obj.get_first_color())]
        return images

    class Meta(ProductSerializers.Meta):
        fields = ["id", "name", "description", "price", "images"]


class ProductDetailSerializers(ProductSerializers):

    product_variants = ProductVariantSerializers(many=True)
    product_images = ProductImageSerializers(many=True)

    class Meta(ProductSerializers.Meta):
        fields = ["id", "name", "description",
                  "product_variants", "product_images"]
