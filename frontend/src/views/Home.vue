<template>
  <div class="home mt-4">
    <Products :products="products" />
  </div>
</template>

<script>
// @ is an alias to /src
import { mapActions, mapState } from "vuex";
import Products from "@/components/Products";
export default {
  name: "Home",
  components: {
    Products,
  },
  methods: {
    ...mapActions(["fetchProducts", "fetchCart"]),
  },
  computed: {
    ...mapState({
      products: (state) => state.product.products,
    }),
  },
  async created() {
    await this.fetchProducts();
  },
};
</script>

<style scoped></style>
