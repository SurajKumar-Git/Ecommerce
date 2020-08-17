<template>
  <div>
    <h3 class="name">{{ product.name }}</h3>
    <p class="description">{{ product.description }}</p>
    <ProductRating :rating="avg_rating" border="dark" />
    <div class="row align-items-center">
      <span class="col-2 heading">Colors:</span>
      <div class="colors col-10">
        <span
          :style="{ background: color.code }"
          class="color mr-3"
          v-for="color in getProductColors"
          :key="color.id"
          :class="{ selected: selected_variant.color.id === color.id }"
          @click="colorSelected(color)"
        ></span>
      </div>
    </div>
    <div class="row align-items-center">
      <span class="col-2 heading">Size:</span>
      <div class="sizes col-10">
        <span
          v-for="size in getProductSize()"
          :key="size.id"
          class="size mr-3"
          :class="{ selected: selected_variant.size.id === size.id }"
          @click="sizeSelected(size)"
        >{{ size.name }}</span>
      </div>
    </div>
    <div v-if="checkInStock">
      <div class="price py-2">&#x20B9; {{ product_inventory.price }}</div>
      <ProductAddToCart v-if="!isProductInCart" />
      <b-button variant="outline-dark" v-else @click="go_to_cart">Go to Cart</b-button>
    </div>
    <div v-else class="out_of_stock">Out of Stock</div>
    <hr />
    <ProductDetailInfo />
    <hr />
    <ProductRatingAndReview />
  </div>
</template>

<script>
import { mapState, mapGetters } from "vuex";
import store from "@/store/index";

import ProductAddToCart from "@/components/ProductAddToCart";
import ProductRating from "@/components/ProductRating";
import ProductRatingAndReview from "@/components/ProductRatingAndReviews";
import ProductDetailInfo from "@/components/ProductDetailInfo";

export default {
  name: "ProductDetail",
  components: {
    ProductAddToCart,
    ProductRating,
    ProductRatingAndReview,
    ProductDetailInfo,
  },
  props: {
    product: {
      type: Object,
      required: true,
    },
  },
  methods: {
    colorSelected(color) {
      store.dispatch("updateSelectVariant", { color });
    },
    sizeSelected(size) {
      store.dispatch("updateSelectVariant", { size });
    },
    go_to_cart() {
      this.$router.push({ name: "Cart" });
    },
  },
  computed: {
    ...mapState({
      selected_variant: (state) => state.product.selected_variant,
      product_inventory: (state) => state.product.product_inventory,
      avg_rating: (state) => state.rating_review.avg_rating,
    }),
    ...mapGetters([
      "getProductColors",
      "getProductSize",
      "checkInStock",
      "getSizes",
      "isProductInCart",
    ]),
  },
  created() {
    store.commit("setDefaultSelectedVariant");
    store.dispatch("fetchProductInventory");
  },
};
</script>

<style scoped>
.name {
  font-weight: 700;
  margin-bottom: 0px;
}

.heading {
  font-weight: 600;
  font-size: large;
}

.price {
  font-size: x-large;
  font-weight: 700;
}

.out_of_stock {
  margin-top: 20px;
  font-size: x-large;
  font-weight: 600;
  color: red;
}

.color {
  height: 35px;
  width: 35px;
  border-radius: 50%;
  display: inline-block;
  border: 1px solid lightgray;
  margin: 5px;
}

.size {
  height: 35px;
  width: 35px;
  display: inline-block;
  border: 1px solid lightgray;
  margin: 5px;
  padding: 5px;
  font-size: large;
  text-align: center;
  vertical-align: middle;
}

.color:hover,
.size:hover {
  border: 1px solid #343a40;
  cursor: pointer;
}

.selected {
  box-shadow: 0 0 0 3px #343a40;
}
</style>
