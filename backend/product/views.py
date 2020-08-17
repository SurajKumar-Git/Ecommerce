from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from .serializers import ProductSerializers, ProductListSerializers, ProductDetailSerializers, ProductVariantSerializers, ProductInventorySerializers, ProductVariantCreateUpdateSerializers
from .serializers import CategorySerilazers
from .models import Product, Color, ProductImage, ProductVariant, ProductInventory, Category
from .permissions import ActionBasedPermission
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = (ActionBasedPermission,)
    filterset_fields = ("category",)
    search_fields = ("name", "description")

    serializer_action_classes = {
        'list': ProductListSerializers,
        'retrieve': ProductDetailSerializers
    }

    action_permissions = {
        IsAdminUser: ['update', 'partial_update', 'destroy', 'create'],
        AllowAny: ["retrieve", 'list']
    }

    def get_serializer_class(self):

        serializer_action_classes = self.serializer_action_classes.get(
            self.action, None)

        return serializer_action_classes if serializer_action_classes else super().get_serializer_class()


class ProductVariantCreateView(CreateAPIView):

    serializer_class = ProductVariantCreateUpdateSerializers
    permission_classes = (IsAdminUser,)


class ProductVariantRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantCreateUpdateSerializers
    permission_classes = (IsAdminUser,)


class ProductInventoryViewSet(viewsets.ModelViewSet):

    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializers
    permission_classes = (ActionBasedPermission,)

    action_permissions = {
        IsAdminUser: ['update', 'partial_update', 'destroy', 'create'],
        AllowAny: ["retrieve"]
    }

    def list(self, request, *args, **kwargs):
        response = {'message': 'List Method is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)


class CategoryListView(ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerilazers
