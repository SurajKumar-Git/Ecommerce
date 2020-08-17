<template>
  <b-row class="mb-4">
    <b-col cols="2">
      <img :src="fullurl(order_item.image)" alt="productImage" width="100px" height="150px" />
    </b-col>
    <b-col cols="6">
      <h4 class="m-0">{{ order_item.product.name }}</h4>
      <p class="m-0">{{ order_item.product.description }}</p>
      <div class="mb-1">
        <b-row align-v="center">
          <b-col cols="2" class="text-muted">Color:</b-col>
          <b-col cols="2">
            <span
              class="color text-left m-1"
              :style="{ background: order_item.product_variant.color.code }"
            ></span>
          </b-col>
        </b-row>
        <b-row align-v="center">
          <b-col cols="2" class="text-muted">Size:</b-col>
          <b-col cols="2" class="text-left">{{ order_item.product_variant.size.name }}</b-col>
        </b-row>
      </div>
      <b-row align-v="center">
        <b-col cols="2" class="text-muted">Price:</b-col>
        <b-col cols="3" class="text-left">&#x20B9; {{ price }}</b-col>
      </b-row>
    </b-col>
    <b-col cols="2" class="text-center">{{ order_item.quantity }}</b-col>
    <b-col cols="2" class="text-center">&#x20B9; {{ total }}</b-col>
  </b-row>
</template>

<script>
export default {
  name: "OrderItem",
  props: {
    order_item: {
      type: Object,
      required: true,
    },
  },
  computed: {
    fullurl() {
      return (url) => this.$store.getters.getFullUrl(url);
    },
    total() {
      return this.order_item.quantity * this.price;
    },
    price() {
      const inventory_price = this.order_item.product_variant.product_inventory
        .price;
      if (inventory_price !== undefined) {
        return inventory_price;
      } else {
        return this.order_item.price;
      }
    },
  },
};
</script>

<style scoped>
.color {
  height: 25px;
  width: 25px;
  border-radius: 50%;
  display: inline-block;
  border: 1px solid lightgray;
}
</style>