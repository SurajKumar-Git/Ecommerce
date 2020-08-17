<template>
  <div class="container mt-5">
    <h3 class="heading">My Orders</h3>
    <hr />
    <div v-if="orders.length !== 0">
      <Order class="mb-4" v-for="order in orders" :key="order.id" :order="order" />
    </div>
    <div v-else class="no_orders">No Orders Placed</div>
  </div>
</template>

<script>
import Order from "@/components/Order";
export default {
  name: "MyOrders",
  components: {
    Order,
  },
  computed: {
    orders() {
      return this.$store.state.order.orders;
    },
  },
  async created() {
    await this.$store.dispatch("fetchOrders");
  },
};
</script>

<style scoped>
.no_orders {
  font-size: larger;
  font-weight: 100;
}
</style>