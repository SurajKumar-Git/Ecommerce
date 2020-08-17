<template>
  <tr>
    <td class="d-flex">
      <div>
        <img :src="fullurl(cartItem.image)" alt="productImage" width="150px" height="200px" />
      </div>
      <div class="ml-3 text-left">
        <h5 class="name">{{ cartItem.product.name }}</h5>
        <p class="description">{{ cartItem.product.description }}</p>
        <div>
          <b-button size="sm" variant="outline-dark" class="mr-3" @click="remove(cartItem)">Remove</b-button>
          <b-button size="sm" variant="outline-dark">Save for Later</b-button>
        </div>
      </div>
    </td>
    <td>
      <b-row align-v="center">
        <b-col class="text-right">Color:</b-col>
        <b-col>
          <span class="color" :style="{ background: cartItem.product_variant.color.code }"></span>
        </b-col>
      </b-row>
      <b-row align-v="center" class="mt-3">
        <b-col class="text-right">Size:</b-col>
        <b-col>{{ cartItem.product_variant.size.name }}</b-col>
      </b-row>
    </td>

    <td>Rs. {{ inventory.price }}</td>
    <td>
      <b-row class="my-1" align-h="center">
        <b-col sm="9">
          <b-form-spinbutton
            class="quantity"
            v-model="cartItem.quantity"
            inline
            min="1"
            :max="inventory.stock"
          ></b-form-spinbutton>
          <p class="error" v-if="error">{{error}}</p>
        </b-col>
      </b-row>
    </td>
    <td>Rs. {{ total }}</td>
  </tr>
</template>

<script>
export default {
  name: "CartItem",
  props: {
    cartItem: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      error: null,
    };
  },
  methods: {
    remove(cartItem) {
      this.$store.dispatch("deleteCartItem", cartItem);
    },
  },
  computed: {
    total() {
      return this.cartItem.quantity * this.inventory.price;
    },
    fullurl() {
      return (url) => this.$store.getters.getFullUrl(url);
    },
    inventory() {
      return this.cartItem.product_variant.product_inventory;
    },
  },
  watch: {
    "cartItem.quantity": async function (new_quantity) {
      this.error = null;
      if (new_quantity !== "") {
        const response = await this.$store.dispatch(
          "changeQuantity",
          this.cartItem
        );
        if (response !== true) {
          this.error = `Invalid Quantity, Available Stock ${response.quantity_error.available_stock}`;
        }
      }
    },
  },
};
</script>

<style scoped>
.name {
  font-weight: 700;
}

.color {
  height: 35px;
  width: 35px;
  border-radius: 50%;
  display: inline-block;
  border: 1px solid lightgray;
}
.quantity {
  margin-top: -10px;
}

.error {
  font-size: small;
  color: red;
  margin-top: 5px;
}
</style>
