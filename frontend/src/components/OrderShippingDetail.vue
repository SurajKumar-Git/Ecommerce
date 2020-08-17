<template>
  <div>
    <h3>Shipping Address</h3>
    <h5 class="mt-2 name">{{ address.full_name }}</h5>
    <p>
      {{ address.address_line1 }}
      <br />
      {{ address.address_line2 }}
      <br />
      {{ address.city }}
      <br />
      {{ address.state }}
      <br />
      {{ address.postal_code }}
      <br />
      Phone No: {{ address.phone }}
      <br />
    </p>
  </div>
</template>

<script>
export default {
  name: "OrderShippingDetail",
  computed: {
    address() {
      return this.$store.state.order.selected_delivery_address;
    },
  },
};
</script>

<style scoped>
.name {
  font-weight: 600;
  margin-bottom: 3px;
}
p {
  line-height: 1.2;
}
</style>