<template>
  <b-nav-item-dropdown text="Category" :no-caret="true">
    <b-dropdown-item @click="filter('')">All</b-dropdown-item>
    <b-dropdown-item
      v-for="category in categories"
      :key="category.id"
      @click="filter(category.id)"
    >{{ category.name }}</b-dropdown-item>
  </b-nav-item-dropdown>
</template>

<script>
export default {
  name: "Category",
  methods: {
    filter(category_id) {
      const params = {
        category: category_id,
      };
      this.$store.dispatch("fetchProducts", params);
    },
  },
  computed: {
    categories() {
      return this.$store.state.product.categories;
    },
  },
  created() {
    this.$store.dispatch("fetchCategories");
  },
};
</script>

<style scoped>
</style>