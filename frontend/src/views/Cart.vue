<template>
  <div>
    <ShoppingCart :cartItems="cartItems" />
  </div>
</template>

<script>
import ShoppingCart from "@/components/ShoppingCart";

export default {
  name: "Cart",
  components: {
    ShoppingCart,
  },
  computed: {
    cartItems() {
      return this.$store.getters.get_cart_items;
    },
  },
};
</script>

<style scoped></style>
