from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework import viewsets
from rest_framework.response import Response

from .models import CartItem
from .serializers import CartItemSerializer, CartItemCreateUpdateSerializer, CartSerializer
# Create your views here.


class CartItemViewSet(viewsets.ModelViewSet):

    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()
    permission_classes = (IsAuthenticated,)

    serializer_action_classes = {
        'create': CartItemCreateUpdateSerializer,
        'update': CartItemCreateUpdateSerializer
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user_cart = self.request.user.user_cart
        return queryset.filter(cart=user_cart)

    def get_serializer_class(self):

        serializer_action_classes = self.serializer_action_classes.get(
            self.action, None)

        return serializer_action_classes if serializer_action_classes else super().get_serializer_class()


class CartView(RetrieveAPIView):

    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = request.user.user_cart
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
