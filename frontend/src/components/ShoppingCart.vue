<template>
  <div class="container mt-5">
    <div class="msg" v-if="message">
      {{ message}}
      <span class="close" @click="close()">x</span>
    </div>
    <h3 class="text-left">My Shopping Cart</h3>
    <hr />
    <div v-if="!isCartEmpty">
      <table class="table text-center table-hover mt-3">
        <thead class="thead-dark">
          <th class="product">Product</th>
          <th class="product_variant">Product Variant</th>
          <th class="text-center">Price</th>
          <th class="quantity">Quantity</th>
          <th>Total</th>
        </thead>
        <tbody>
          <CartItem v-for="cartItem in cartItems" :key="cartItem.id" :cartItem="cartItem" />
        </tbody>
      </table>
      <div class="total">
        <b-row class="total_amount">
          <b-col class="text-right">Total Amount</b-col>
          <b-col>Rs. {{cart_items_total}}</b-col>
        </b-row>
      </div>
      <hr />
      <div class="text-right mt-4">
        <b-button variant="outline-dark" class="mr-3" :to="{name: 'Home'}">Continue Shopping</b-button>
        <b-button variant="dark" :to="{name: 'SelectAddress'}">Place Order</b-button>
      </div>
    </div>
    <div v-else class="text-center">
      No Items in Cart
      <div class="home">
        <router-link :to="{name:'Home'}">Continue Shopping</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import CartItem from "@/components/CartItem";
export default {
  name: "ShoppingCart",
  props: {
    cartItems: {
      type: Array,
      required: true,
    },
  },
  components: {
    CartItem,
  },
  computed: {
    cart_items_total() {
      return this.$store.getters.cart_items_total;
    },
    message() {
      return this.$store.getters.getOrderSuccessMsg;
    },
    isCartEmpty() {
      return this.$store.getters.isCartEmpty;
    },
  },
  methods: {
    close() {
      this.$store.commit("clearOrderSuccessMsg");
    },
  },
  destroyed() {
    this.close();
  },
};
</script>

<style scoped>
.home {
  font-size: larger;
}
.product {
  width: 450px;
}
.product_variant {
  width: 180px;
}

.table thead th {
  border-bottom: none;
}

.table tr:last-child {
  border-bottom: 1px solid #dee2e6;
}

.total {
  width: 30%;
  margin-left: auto;
}

.total .row:last-child {
  font-size: larger;
  font-weight: 700;
  color: #343a40;
}

.msg {
  border: 1px solid #28a745;
  border-radius: 5px;
  padding: 10px 10px;
  margin-bottom: 15px;
}

.close {
  margin-right: auto;
}
.close:hover {
  cursor: pointer;
}
</style>
