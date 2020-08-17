import httpClient from "@/AxiosConfig";

export default {
  state: {
    avg_rating: 0,
    rating_and_reviews: [],
    user_rating_and_review: {
      rating: 0,
      review: "",
    },
  },
  getters: {},
  mutations: {
    setRatingAndReviews(state, rating_and_reviews) {
      state.rating_and_reviews = rating_and_reviews;
    },
    setAvgRating(state, avg_rating) {
      state.avg_rating = avg_rating.avg_rating;
    },
    setUserRatingAndReview(state, user_rating_and_review) {
      const index = state.rating_and_reviews.findIndex((rating_and_review) => {
        return rating_and_review.id === user_rating_and_review.id;
      });
      state.rating_and_reviews.splice(index, 1);
      state.rating_and_reviews.unshift(user_rating_and_review);
      state.user_rating_and_review = user_rating_and_review;
    },
  },
  actions: {
    async fetchRatingAndReview({ commit }, product_id) {
      const response = await httpClient.get(
        `rating_review/RatingAndReview/product/${product_id}/`
      );
      commit("setRatingAndReviews", response.data);
    },
    async fetchAvgRating({ commit }, product_id) {
      const response = await httpClient.get(
        `rating_review/RatingAndReview/product/${product_id}/avg_rating/`
      );
      if (response.data.avg_rating !== null) {
        commit("setAvgRating", response.data);
      }
    },
    async fetchUserRatingAndReview({ commit }, product_id) {
      const response = await httpClient.get(
        `rating_review/RatingAndReview/product/${product_id}/user/`
      );
      if (response.data.rating != null) {
        commit("setUserRatingAndReview", response.data);
      }
    },
    async postRatingAndReview({ commit, dispatch }, payload) {
      try {
        const response = await httpClient.post(
          "rating_review/RatingAndReview/",
          payload
        );
        commit("setUserRatingAndReview", response.data);
        await dispatch("fetchAvgRating", response.data.product);
      } catch (error) {
        console.log(error.response);
      }
    },
  },
};
