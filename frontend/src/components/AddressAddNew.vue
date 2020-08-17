<template>
  <div class="w-75">
    <b-form @submit.prevent="add_new_address" class="mt-3">
      <b-form-group label="Full Name:" label-for="full_name">
        <b-form-input
          id="full_name"
          v-model="address_form.full_name"
          type="text"
          required
          placeholder="Enter Full Name"
        ></b-form-input>
      </b-form-group>

      <b-form-group label="Address Line 1" label-for="address_line1">
        <b-form-input
          id="address_line1"
          v-model="address_form.address_line1"
          type="text"
          required
          placeholder="#No, Building Name"
        ></b-form-input>
      </b-form-group>

      <b-form-group label="Address Line 2" label-for="address_line2">
        <b-form-input
          id="address_line2"
          v-model="address_form.address_line2"
          type="text"
          required
          placeholder="Street, Area"
        ></b-form-input>
      </b-form-group>

      <b-form-group label="City" label-for="city">
        <b-form-input id="city" v-model="address_form.city" type="text" required placeholder="City"></b-form-input>
      </b-form-group>

      <b-form-group label="State" label-for="state">
        <b-form-input
          id="state"
          v-model="address_form.state"
          type="text"
          required
          placeholder="State"
        ></b-form-input>
      </b-form-group>

      <b-form-group label="Postal Code" label-for="postal_code">
        <b-form-input
          id="postal_code"
          v-model="address_form.postal_code"
          type="text"
          required
          placeholder="Postal Code"
        ></b-form-input>
      </b-form-group>
      <b-button type="submit" variant="outline-dark">Add & Deliver here</b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  name: "AddressAddNew",
  data() {
    return {
      address_form: {
        full_name: null,
        address_line1: null,
        address_line2: null,
        city: null,
        state: null,
        postal_code: null,
      },
    };
  },
  methods: {
    async add_new_address(event) {
      await this.$store.dispatch("addNewAddress", this.address_form);
      this.$emit("select-delivery-address", this.address_form);
      event.target.reset();
    },
    delivery_address(address) {
      this.$store.commit("setDeliveryAddress", address);
      this.$router.push({ name: "Order" });
    },
  },
};
</script>

<style scoped>
</style>