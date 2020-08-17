<template>
  <div>
    Cart <b-icon icon="cart" v-if="cart_empty"></b-icon>
    <b-icon icon="cart-fill" v-else></b-icon>
  </div>
</template>

<script>
export default {
  name: "CartIcon",
  computed: {
    cart_empty() {
      return this.$store.getters.isCartEmpty;
    },
  },
};
</script>
