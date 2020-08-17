<template>
  <div>
    <div>
      <h3>Payment Method</h3>
      <p class="mt-2">Cash on Delivery</p>
    </div>
    <div>
      <h3>Expected Delivery Date</h3>
      <p>{{ delivery_date }}</p>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    delivery_date() {
      let today = new Date();
      today.setDate(today.getDate() + 2);
      return today.toDateString();
    },
  },
};
</script>