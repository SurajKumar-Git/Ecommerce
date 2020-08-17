from django.urls import path, include
from rest_framework import routers
from .views import CartItemViewSet, CartView


router_default = routers.DefaultRouter()

router_default.register(r"cartitem", CartItemViewSet, basename="cart_item")

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('', include(router_default.urls)),

]
