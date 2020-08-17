from rest_framework import serializers

from product.serializers import ProductVariantSerializers, ProductSerializers
from product.models import ProductVariant, ProductInventory, ProductImage

from user.models import Address
from user.serializers import AddressSerializer, UserFilteredPrimaryKeyRelatedField


from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

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
        model = OrderItem
        fields = ("product", "image", "product_variant", "quantity", "price")
        read_only_fields = ('product', 'image')


class OrderItemCreateSerializer(OrderItemSerializer):

    product_variant = serializers.PrimaryKeyRelatedField(
        queryset=ProductVariant.objects.all())

    def validate(self, data):
        variant = data.get("product_variant")
        quantity = data.get("quantity")
        in_stock, stock = ProductInventory.inventory.check_stock(
            variant, quantity)
        if not in_stock:
            raise serializers.ValidationError("Product Out of Stock")
        return data


class OrderSerializer(serializers.ModelSerializer):

    order_items = OrderItemSerializer(many=True)
    shipping_address = AddressSerializer()
    ord_no = serializers.SerializerMethodField()

    def get_ord_no(self, obj):
        return f"ORD_{obj.id}_RC_{obj.created.strftime('%d%m%Y')}"

    class Meta:
        model = Order
        fields = ("id", "ord_no", "user", "shipping_address",
                  "status", "created", "order_items")
        read_only_fields = ("id", "user", "ord_no")


class OrderCreateSerializer(OrderSerializer):

    order_items = OrderItemCreateSerializer(many=True)
    shipping_address = UserFilteredPrimaryKeyRelatedField(
        queryset=Address.objects.all())

    class Meta(OrderSerializer.Meta):
        read_only_fields = ("id", "ord_no", "user", "status")

    def create(self, validated_data):

        order_items = validated_data.pop("order_items")

        user = self.context["request"].user
        order = Order.objects.create(user=user, **validated_data)

        for order_item in order_items:
            variant = order_item.get("product_variant")
            quantity = order_item.get("quantity")
            ProductInventory.inventory.update_stock(variant, quantity)
            OrderItem.objects.create(order=order, **order_item)

        user.user_cart.clear_cart()

        return order


class OrderUpdateSerializer(OrderSerializer):

    order_items = OrderItemCreateSerializer(many=True)
    shipping_address = UserFilteredPrimaryKeyRelatedField(
        queryset=Address.objects.all())

    class Meta(OrderSerializer.Meta):
        fields = ("status",)
