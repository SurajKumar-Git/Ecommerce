from django.urls import include, path
from rest_framework import routers
# from .views import ProductViewSet, ProductInventoryViewSet, ProductVariantViewSet, CategoryListView
from .views import (ProductViewSet,
                    CategoryListView,
                    ProductInventoryViewSet,
                    ProductVariantCreateView,
                    ProductVariantRetrieveUpdateDestroyView)

router = routers.DefaultRouter()

router.register("product", ProductViewSet)
router.register("productinventory", ProductInventoryViewSet)
# router.register("ProductVariant", ProductVariantViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("productvariant/", ProductVariantCreateView.as_view(),
         name="product_variant_Create"),
    path("productvariant/<int:pk>/", ProductVariantRetrieveUpdateDestroyView.as_view(),
         name="product_variant_RetrieveUpdateDestroy"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
