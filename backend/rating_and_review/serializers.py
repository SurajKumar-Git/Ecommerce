from rest_framework import serializers

from product.models import Product
from .models import RatingAndReview

from datetime import date


class RatingAndReviewSerializer(serializers.ModelSerializer):

    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all())

    user = serializers.CharField(source="user.get_full_name", read_only=True)

    modified = serializers.SerializerMethodField()

    def get_modified(self, obj):
        return (date.today() - obj.modified).days

    class Meta:
        model = RatingAndReview
        fields = ("id", "rating", "title", "review",
                  "user", "product", "created", "modified")
        read_only_fields = ("user", "title", "created", "modified")

    def create(self, validated_data):
        user = self.context["request"].user
        rating_review = RatingAndReview.rating_reviews.add(
            user=user, **validated_data)
        return rating_review


class RatingAndReviewUpdateSerializer(RatingAndReviewSerializer):

    class Meta(RatingAndReviewSerializer.Meta):
        read_only_fields = ("user", "product", "title", "created", "modified")

    def update(self, instance, validated_data):
        rating_review = RatingAndReview.rating_reviews.update(
            **validated_data, rating_review=instance)
        return rating_review


class AvgRatingSerializer(serializers.Serializer):
    avg_rating = serializers.FloatField(min_value=1, max_value=5)
