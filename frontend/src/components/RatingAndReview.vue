<template>
  <div>
    <b-card header-bg-variant="dark">
      <template v-slot:header>
        <ProductRating :rating="rating_and_review.rating" border="light" />
        <h6 class="title">{{ rating_and_review.title }}</h6>
      </template>
      <b-card-text>{{ rating_and_review.review }}</b-card-text>
      <p class="text-muted footer">- {{ rating_and_review.user }} - {{ modified_date }}</p>
    </b-card>
  </div>
</template>

<script>
import ProductRating from "@/components/ProductRating";

export default {
  name: "RatingAndReview",
  props: {
    rating_and_review: {
      type: Object,
      required: true,
    },
  },
  components: {
    ProductRating,
  },
  computed: {
    modified_date() {
      if (this.rating_and_review.modified == 0) {
        return "Today";
      } else if (this.rating_and_review.modified == 1) {
        return `${this.rating_and_review.modified} day ago`;
      } else {
        return `${this.rating_and_review.modified} days ago`;
      }
    },
  },
};
</script>

<style scoped>
.title {
  margin: 0;
  margin-left: 15px;
  display: inline-block;
  font-weight: 500;
  color: white;
}
.footer {
  margin: 0;
}
</style>