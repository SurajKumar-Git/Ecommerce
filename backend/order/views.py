from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer, OrderCreateSerializer, OrderUpdateSerializer
from .permissions import ChangeOrderStatusPermission

# Create your views here.


class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, ChangeOrderStatusPermission)

    serializer_action_classes = {
        'create': OrderCreateSerializer,
        'update': OrderUpdateSerializer
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_serializer_class(self):

        serializer_action_classes = self.serializer_action_classes.get(
            self.action, None)

        return serializer_action_classes if serializer_action_classes else super().get_serializer_class()
