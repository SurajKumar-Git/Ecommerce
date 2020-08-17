<template>
  <b-card title="Order Summary" class="total">
    <hr />
    <div>
      <b-row class="my-2">
        <b-col cols="8">SubTotal</b-col>
        <b-col>&#x20B9; {{order_items_total}}</b-col>
      </b-row>
      <b-row class="my-2">
        <b-col cols="8">Shipping Charges</b-col>
        <b-col>&#x20B9; 0</b-col>
      </b-row>
      <b-row class="my-2">
        <b-col cols="8">Tax</b-col>
        <b-col>&#x20B9; 0</b-col>
      </b-row>
      <hr />
      <b-row class="total_amount my-2">
        <b-col cols="8">Total Amount</b-col>
        <b-col>&#x20B9; {{order_items_total}}</b-col>
      </b-row>
    </div>
    <b-button variant="outline-dark" class="mt-2 px-3 py-2" @click="placeOrder">Confirm Order</b-button>
  </b-card>
</template>

<script>
export default {
  name: "OrderSummary",
  props: {
    order_items: {
      type: Array,
      required: true,
    },
  },
  computed: {
    order_items_total() {
      return this.$store.getters.cart_items_total;
    },
  },
  methods: {
    placeOrder() {
      const payload_order_items = [];
      for (let order_item of this.order_items) {
        payload_order_items.push({
          product_variant: order_item.product_variant.id,
          quantity: order_item.quantity,
          price: order_item.product_variant.product_inventory.price,
        });
      }
      const order = {
        shipping_address: this.$store.state.order.selected_delivery_address.id,
        order_items: payload_order_items,
      };
      this.$store.dispatch("placeOrder", order);
      this.$router.push({ name: "Cart" });
    },
  },
};
</script>

<style scoped>
.total {
  width: 85%;
  margin: auto;
}

.total_amount {
  font-size: large;
  font-weight: 700;
}
</style>