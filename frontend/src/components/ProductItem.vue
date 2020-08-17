<template>
  <router-link :to="{ name: 'Product', params: { product_id: product.id } }" class="product-card">
    <b-card @mouseover="setInterval()" @mouseout="removeInterval()" class="h-100">
      <template v-slot:header>
        <b-carousel :id="'product' + product.id" :interval="interval" indicators no-hover-pause>
          <b-carousel-slide
            v-for="(image, index) in product.images"
            :img-src="getFullUrl(image)"
            :key="index"
          ></b-carousel-slide>
        </b-carousel>
      </template>
      <b-card-title :title="product.name"></b-card-title>
      <b-card-text>
        <p class="product_desc">{{ product.description }}</p>
        <p class="product_price">Rs. {{ product.price }}</p>
      </b-card-text>
    </b-card>
  </router-link>
</template>

<script>
export default {
  name: "ProductItem",
  props: {
    product: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      interval: null,
    };
  },
  methods: {
    setInterval() {
      this.interval = "1000";
    },
    removeInterval() {
      this.interval = 0;
    },
    getFullUrl: (url) => {
      return "http://127.0.0.1:5000".concat(url);
    },
  },
};
</script>

<style scoped>
.product-card {
  color: black;
}

.product-card:hover {
  text-decoration: none;
}

.card-header {
  padding: 0;
}

.carousel-indicators li {
  width: 3px;
}

.card-body {
  text-align: left;
  padding: 10px;
  padding-bottom: 0;
}
.card-title {
  font-weight: 700;
  margin-bottom: 4px;
}

.product_desc {
  margin-bottom: 4px;
  font-size: medium;
  color: gray;
}

.product_price {
  margin-bottom: 4px;
  font-size: medium;
  font-weight: 700;
}
</style>
