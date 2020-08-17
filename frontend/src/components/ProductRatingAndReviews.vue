<template>
  <div class="ratings">
    <div class="top-bar mb-3 d-flex justify-content-between">
      <h4>Rating & Reviews</h4>
      <RatingAndReviewForm />
    </div>
    <div class="d-flex flex-column cards" v-if="rating_and_reviews_exists">
      <RatingAndReview
        v-for="rating_and_review in rating_and_reviews"
        :key="rating_and_review.id"
        :rating_and_review="rating_and_review"
      />
    </div>
    <div v-else class="cards">
      <p class="text">No Rating and Reviews</p>
    </div>
  </div>
</template>

<script>
import RatingAndReview from "@/components/RatingAndReview";
import RatingAndReviewForm from "@/components/RatingAndReviewForm";

export default {
  name: "ProductRatingAndReview",
  components: {
    RatingAndReview,
    RatingAndReviewForm,
  },
  computed: {
    rating_and_reviews() {
      return this.$store.state.rating_review.rating_and_reviews;
    },
    rating_and_reviews_exists() {
      return this.rating_and_reviews.length !== 0;
    },
  },
};
</script>

<style scoped>
.ratings {
  margin-top: 15px;
  border: 1px solid lightgray;
}

.cards {
  padding: 10px;
}

.top-bar {
  background: #343a40;
  padding: 8px;
}

.top-bar h4 {
  color: white;
  padding: 8px;
  display: inline-block;
  margin: 0;
}

.top-bar div {
  display: inline-block;
  align-self: center;
}
.text {
  font-size: large;
  padding-left: 10px;
}
</style>