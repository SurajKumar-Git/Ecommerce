<template>
  <b-card :title="address.full_name" class="mb-4 h-100">
    <b-card-text>
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
    </b-card-text>
    <b-button
      size="sm"
      variant="outline-dark"
      @click="$emit('select-delivery-address', address)"
    >Deliver here</b-button>
  </b-card>
</template>

<script>
export default {
  name: "Address",
  props: {
    address: {
      type: Object,
      required: true,
    },
  },
  methods: {
    delivery_address(address) {
      this.$store.commit("setDeliveryAddress", address);
      this.$router.push({ name: "Order" });
    },
  },
};
</script>


<style scoped>
</style>