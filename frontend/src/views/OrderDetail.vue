<template>
  <div class="container mt-5">
    <h3>Order Detail</h3>
    <b-row class="mt-3">
      <b-col cols="8">
        <OrderItemList :order_items="order_items" />
      </b-col>
      <b-col cols="4">
        <OrderSummary :order_items="order_items" />
      </b-col>
    </b-row>
    <hr />
    <b-row class="mt-5">
      <b-col>
        <OrderShippingDetail />
      </b-col>
      <b-col>
        <OrderPaymentMethod />
      </b-col>
    </b-row>
  </div>
</template>

<script>
import OrderItemList from "@/components/OrderItemList";
import OrderSummary from "@/components/OrderSummary";
import OrderShippingDetail from "@/components/OrderShippingDetail";
import OrderPaymentMethod from "@/components/OrderPaymentMethod";

export default {
  name: "OrderDetail",
  components: {
    OrderItemList,
    OrderSummary,
    OrderShippingDetail,
    OrderPaymentMethod,
  },
  data() {
    return {
      order_items: [],
    };
  },

  created() {
    this.order_items = this.$store.state.cart.cart_items;
  },
};
</script>

<style scoped>
</style>