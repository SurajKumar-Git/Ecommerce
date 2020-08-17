from django.urls import path, include
from .views import UserDetailView, UserAddressView, UserRegistrationView
from rest_framework import routers

router = routers.DefaultRouter()

router.register("address", UserAddressView)

urlpatterns = [
    path("", UserDetailView.as_view(), name="user_detail"),
    path("register/", UserRegistrationView.as_view(), name="registration"),
    path("", include(router.urls))

]
