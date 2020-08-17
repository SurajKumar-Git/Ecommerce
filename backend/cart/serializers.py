from rest_framework import serializers

from .models import CartItem, Cart
from product.models import ProductVariant, ProductInventory, ProductImage
from product.serializers import ProductVariantSerializers, ProductSerializers


class CartItemSerializer(serializers.ModelSerializer):

    product = serializers.SerializerMethodField()
    product_variant = ProductVariantSerializers()
    image = serializers.SerializerMethodField()

    def get_product(self, obj):
        product = obj.product_variant.product
        return ProductSerializers(product).data

    def get_image(self, obj):
        color = obj.product_variant.color
        product = obj.product_variant.product
        return ProductImage.productimages.get_image(color, product).url

    class Meta:
        model = CartItem
        fields = ["id", "image", "product", "product_variant", "quantity"]


class CartItemCreateUpdateSerializer(CartItemSerializer):

    product_variant = serializers.PrimaryKeyRelatedField(
        queryset=ProductVariant.objects.all())

    class Meta(CartItemSerializer.Meta):
        fields = ["id", "image", "product", "product_variant", "quantity"]
        read_only_fields = ['id', "image", "product"]

    def validate(self, data):
        quantity = data.get("quantity")
        variant = data.get("product_variant")
        in_stock, stock = ProductInventory.inventory.check_stock(
            variant,
            quantity
        )
        if not in_stock:
            raise serializers.ValidationError(
                detail={"quantity_error": {"available_stock": stock}})
        return super().validate(data)

    def create(self, validated_data):

        cart = self.context['request'].user.user_cart
        cart_item = CartItem.cart_items.check_in_cart(
            cart, validated_data["product_variant"])
        if not cart_item:
            cart_item = CartItem.objects.create(cart=cart, **validated_data)
        return cart_item

    def update(self, instance, validated_data):
        instance.product_variant = validated_data.get(
            "product_variant", instance.product_variant)
        instance.quantity = validated_data.get("quantity", instance.quantity)
        instance.save()
        return instance


class CartSerializer(serializers.ModelSerializer):

    cart_items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ["id", "cart_items"]
