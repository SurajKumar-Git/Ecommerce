from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import RatingAndReviewViewSet

router = DefaultRouter()

router.register("RatingAndReview", RatingAndReviewViewSet)

urlpatterns = [
    path("", include(router.urls))
]
