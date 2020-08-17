<template>
  <b-container>
    <b-row cols="4">
      <b-col v-for="product in products" :key="product.id" class="mb-4">
        <ProductItem :product="product" />
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import ProductItem from "@/components/ProductItem";

export default {
  name: "Products",
  components: {
    ProductItem,
  },
  props: {
    products: {
      type: Array,
      required: true,
    },
  },
};
</script>
