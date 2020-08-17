from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Avg

from django.core.validators import MinValueValidator, MaxValueValidator

from product.models import Product
# Create your models here.


class RatingAndReviewQuerySet(models.QuerySet):

    def get_given_rating_review(self, user, product):
        try:
            return self.get(user=user, product=product)
        except(RatingAndReview.DoesNotExist):
            return None

    def is_rating_review_given(self, user, product):
        rating_review = self.get_given_rating_review(
            user=user, product=product)
        return (True, rating_review) if rating_review else (False, None)

    def add(self, **kwargs):
        exists, rating_review = self.is_rating_review_given(
            kwargs.get("user"), kwargs.get("product"))
        if not exists:
            return self.create(**kwargs)
        else:
            return self.update(rating_review=rating_review, **kwargs)

    def update(self, **kwargs):
        rating_review = kwargs.get("rating_review")
        rating_review.rating = kwargs.get("rating")
        rating_review.review = kwargs.get("review")
        rating_review.save()
        return rating_review

    def product_rating_reviews(self, product_id):
        return self.filter(product__id=product_id)

    def product_avg_rating(self, product_id):
        return self.product_rating_reviews(product_id).aggregate(avg_rating=Avg('rating'))


class RatingAndReview(models.Model):

    title_choice = {1: "Very Bad", 2: "Bad",
                    3: "Good", 4: "Very Good", 5: "Excellent"}

    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    title = models.CharField(max_length=128)
    review = models.CharField(max_length=1024)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    objects = models.Manager()
    rating_reviews = RatingAndReviewQuerySet.as_manager()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        title = self.title_choice.get(self.rating)
        self.title = title
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    class Meta:
        ordering = ('-modified',)
