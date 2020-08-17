<template>
  <div>
    <b-button variant="outline-light" size="sm" @click="showRatingForm">Rate & Review The Product</b-button>
    <b-modal
      id="form"
      title="Rate and Review"
      size="lg"
      centered
      button-size="sm"
      ok-title="Submit"
      header-bg-variant="dark"
      header-text-variant="light"
      @cancel="show_cancel"
      @show="show_cancel"
      @ok="submit"
    >
      <b-form>
        <b-form-group label="Rate this product" label-for="rating" label-cols="3">
          <b-form-rating id="rating" inline v-model="form.rating" size="lg" no-border name="rating"></b-form-rating>
          <p class="error pl-4" v-if="error.rating">{{ error.rating }}</p>
        </b-form-group>

        <b-form-group label="Review this product" label-for="review">
          <b-form-textarea
            id="review"
            v-model="form.review"
            :state="review_within_limit"
            placeholder="Leave some review on this product"
            rows="3"
            max-rows="6"
            required
          ></b-form-textarea>
          <p class="error" v-if="error.review">{{ error.review }}</p>
        </b-form-group>
      </b-form>
      <template v-slot:modal-footer="{ ok, cancel }">
        <b-button size="sm" variant="dark" @click="cancel()">Cancel</b-button>
        <b-button size="sm" variant="outline-dark" @click="ok()">Submit</b-button>
      </template>
    </b-modal>
  </div>
</template>

<script>
export default {
  name: "RatingAndReviewForm",
  data() {
    return {
      form: {
        rating: 0,
        review: "",
      },
      error: {
        rating: null,
        review: null,
      },
    };
  },
  methods: {
    async showRatingForm() {
      const user_is_authenticated = this.$store.state.user.isAuthenticated;
      if (user_is_authenticated) {
        this.updateRatingForm();
        this.$bvModal.show("form");
      } else {
        this.$store.commit("setNeedAuthentication");
      }
    },
    submit(event) {
      event.preventDefault();
      if (this.form.rating > 0 && this.review_within_limit) {
        const data = {
          ...this.form,
          product: this.$store.state.product.product.id,
        };
        this.$store.dispatch("postRatingAndReview", data);
        this.$nextTick(() => {
          this.$bvModal.hide("form");
        });
      } else {
        if (this.form.rating == 0) {
          this.error.rating = "This field is reqired";
        }
        if (!this.review_within_limit) {
          this.error.review = "Require atleast 10 Chars";
        }
        return;
      }
    },
    show_cancel() {
      this.error.rating = "";
      this.error.review = "";
    },
    async updateRatingForm() {
      const product_id = this.$store.state.product.product.id;
      await this.$store.dispatch("fetchUserRatingAndReview", product_id);
      this.form.rating = this.$store.state.rating_review.user_rating_and_review.rating;
      this.form.review = this.$store.state.rating_review.user_rating_and_review.review;
    },
  },
  computed: {
    review_within_limit() {
      return this.form.review.length >= 5 && this.form.review.length <= 1024;
    },
  },
  created() {
    this.form.rating = this.$store.state.rating_review.user_rating_and_review.rating;
    this.form.review = this.$store.state.rating_review.user_rating_and_review.review;
  },
};
</script>

<style scoped>
.error {
  font-size: small;
  color: red;
  margin: 0;
}
</style>