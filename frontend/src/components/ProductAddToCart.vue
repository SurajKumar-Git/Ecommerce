<template>
  <div>
    <div class="row align-items-center">
      <span class="col-2 heading">Quantity:</span>
      <div class="col-10">
        <b-form-spinbutton v-model="quantity" inline min="1" :max="stock"></b-form-spinbutton>
      </div>
    </div>
    <b-button variant="outline-dark" @click="add_to_cart()" class="add_to_cart my-3">Add to Cart</b-button>
  </div>
</template>

<script>
export default {
  name: "ProductAddToCart",
  data() {
    return {
      quantity: 1,
    };
  },
  methods: {
    async add_to_cart() {
      const user_is_authenticated = this.$store.state.user.isAuthenticated;
      if (user_is_authenticated) {
        const variant = this.$store.state.product.selected_variant;
        await this.$store.dispatch("addProductToCart", {
          product_variant: variant.id,
          quantity: this.quantity,
        });
      } else {
        this.$store.commit("setNeedAuthentication");
      }
    },
  },
  computed: {
    stock() {
      return this.$store.state.product.product_inventory.stock;
    },
  },
};
</script>

<style scoped>
.heading {
  font-weight: 600;
  font-size: large;
}

.add_to_cart {
  font-weight: 600;
}
</style>