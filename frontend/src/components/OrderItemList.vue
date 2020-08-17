<template>
  <div class="d-flex flex-column">
    <b-row class="headings mb-4">
      <b-col cols="8">Product</b-col>
      <b-col cols="2" class="text-center">Quantity</b-col>
      <b-col cols="2" class="text-center">Total</b-col>
    </b-row>
    <OrderItem v-for="order_item in order_items" :key="order_item.id" :order_item="order_item" />
  </div>
</template>


<script>
import OrderItem from "@/components/OrderItem";

export default {
  name: "OrderItemList",
  components: { OrderItem },
  props: {
    order_items: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped>
.headings {
  background: #2c3e50;
  height: 40px;
}
.headings div {
  font-size: large;
  font-weight: 700;
  color: white;
  padding: 8px 15px;
}
</style>