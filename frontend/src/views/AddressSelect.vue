<template>
  <div class="container mt-4">
    <div>
      <h4>Select Delivery Address</h4>
      <b-row cols="4" class="mt-4">
        <b-col v-for="address in addresses" :key="address.id">
          <Address :address="address" @select-delivery-address="delivery_address" />
        </b-col>
      </b-row>
    </div>
    <p class="h-line mt-5">
      <span>Or</span>
    </p>
    <div class="my-5">
      <h4>Add New Address</h4>
      <AddressAddNew @select-delivery-address="delivery_address" />
    </div>
  </div>
</template>

<script>
import Address from "@/components/Address";
import AddressAddNew from "@/components/AddressAddNew";

export default {
  name: "AddressSelect",
  components: {
    Address,
    AddressAddNew,
  },
  methods: {
    delivery_address(address) {
      this.$store.commit("setDeliveryAddress", address);
      this.$router.push({ name: "Order" });
    },
  },
  computed: {
    addresses() {
      return this.$store.state.user.addresses;
    },
  },
  async created() {
    await this.$store.dispatch("fetchUserAddresses");
  },
};
</script>

<style scoped>
.h-line {
  text-align: center;
  border-bottom: 1px solid lightgray;
  line-height: 0.1em;
}
.h-line span {
  font-size: large;
  font-weight: 700;
  background: #fff;
  padding: 0 10px;
  color: lightgray;
}
</style>