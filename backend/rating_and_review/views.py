from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status

from .models import RatingAndReview
from .serializers import RatingAndReviewSerializer, RatingAndReviewUpdateSerializer, AvgRatingSerializer

from product.models import Product
# Create your views here.


class RatingAndReviewViewSet(ModelViewSet):

    serializer_class = RatingAndReviewSerializer
    queryset = RatingAndReview.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    serializer_action_classes = {
        'update': RatingAndReviewUpdateSerializer
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        response = {'message': 'List Method is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    @ action(detail=False, url_path=r"product/(?P<product_id>[^/.]+)", url_name="product_rating_review")
    def product_rating_review(self, request, **kwargs):
        product_id = kwargs["product_id"]
        queryset = RatingAndReview.rating_reviews.product_rating_reviews(
            product_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, url_path=r"product/(?P<product_id>[^/.]+)/avg_rating", url_name="avg_product_rating")
    def avg_product_rating(self, request, **kwargs):
        product_id = kwargs["product_id"]
        data = RatingAndReview.rating_reviews.product_avg_rating(product_id)
        serialized = AvgRatingSerializer(data)
        return Response(serialized.data)

    @action(detail=False, url_path="product/(?P<product_id>[^/.]+)/user", url_name='user_product_rating_review')
    def user_product_rating_review(self, request, **kwargs):
        user = request.user
        if user.is_authenticated:
            product = Product.objects.get(id=kwargs["product_id"])
            data = RatingAndReview.rating_reviews.get_given_rating_review(
                user, product)
            serializer = self.get_serializer(data)
            return Response(serializer.data)
        return Response({})
