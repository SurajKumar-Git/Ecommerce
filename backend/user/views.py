from django.shortcuts import render
from django.contrib.auth import get_user_model


from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Address
from .serializers import UserSerializer, AddressSerializer, UserRegistrationSerializer
# Create your views here.


class UserDetailView(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UserRegistrationView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegistrationSerializer


class UserAddressView(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Address.objects.filter(user=self.request.user)
        return queryset
