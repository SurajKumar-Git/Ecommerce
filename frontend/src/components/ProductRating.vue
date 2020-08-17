<template>
  <div
    class="border rounded bg-dark d-inline-flex align-items-center star"
    :class="`border-${border}`"
    v-if="rating"
  >
    <span class="text-light mx-2 avg align-self-center">{{rating}}</span>
    <b-icon icon="star-fill" class="mr-2 mb-1" variant="light"></b-icon>
  </div>
</template>

<script>
export default {
  name: "ProductRating",
  props: {
    rating: {
      type: Number,
      required: true,
    },
    border: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped>
.star {
  font-size: medium;
}
.avg {
  font-weight: 700;
}
</style>