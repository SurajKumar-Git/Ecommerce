<template>
  <b-container class="mt-5">
    <b-row>
      <b-col>
        <ProductDetailImages />
      </b-col>
      <b-col>
        <ProductDetail :product="product" />
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import { mapState } from "vuex";
import ProductDetail from "@/components/ProductDetail";
import ProductDetailImages from "@/components/ProductDetailImages";
import store from "@/store/index";

export default {
  name: "Product",
  data() {
    return {
      loaded: false,
    };
  },
  components: {
    ProductDetail,
    ProductDetailImages,
  },
  computed: {
    ...mapState({
      product: (state) => state.product.product,
    }),
  },
  async beforeRouteEnter(to, from, next) {
    const product_id = to.params.product_id;
    await store.dispatch("fetchProductDetail", product_id);
    await store.dispatch("fetchAvgRating", product_id);
    await store.dispatch("fetchRatingAndReview", product_id);
    next();
  },
};
</script>

<style scoped></style>
