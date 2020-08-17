<template>
  <div>
    <b-card no-body>
      <b-card-header header-bg-variant="light" class="d-flex justify-content-between">
        <p>Order #{{order.ord_no}}</p>
        <p class="text-muted">Order Place on {{created}}</p>
        <p v-if="!cancelled">
          Cancel Order
          <button
            type="button"
            class="close ml-2 click"
            @click="cancel(order.id)"
            aria-label="Close"
          >
            <span aria-hidden="true">&times;</span>
          </button>
        </p>
      </b-card-header>
      <b-card-body>
        <div class="d-flex flex-column">
          <b-row class="headings">
            <b-col cols="8">Product</b-col>
            <b-col cols="2" class="text-center">Quantity</b-col>
            <b-col cols="2" class="text-center">Total</b-col>
          </b-row>
          <OrderItem
            v-for="order_item in order.order_items"
            :key="order_item.id"
            :order_item="order_item"
          />
        </div>
      </b-card-body>
      <b-card-footer footer-bg-variant="light" class="d-flex justify-content-between">
        <p class="font-weight-bold">Status: {{order_status}}</p>
        <p :id="'shipping_address'+order.id" class="click">Shipping Address</p>
        <p :id="'payment'+order.id" class="click">Payment Method</p>
        <p class="font-weight-bold">Total Amount: &#x20B9; {{total_amount}}</p>
      </b-card-footer>
    </b-card>
    <b-popover :target="'shipping_address'+order.id" triggers="hover" placement="top">
      <p class="address">
        <span class="full_name">{{ address.full_name }}</span>
        <br />
        {{ address.address_line1 }}
        <br />
        {{ address.address_line2 }}
        <br />
        {{ address.city }}
        <br />
        {{ address.state }}
        <br />
        {{ address.postal_code }}
        <br />
        Phone No: {{ address.phone }}
        <br />
      </p>
    </b-popover>
    <b-popover :target="'payment'+order.id" triggers="hover" placement="top">
      <p>Cash On Delivery</p>
    </b-popover>
  </div>
</template>

<script>
import OrderItem from "@/components/OrderItem";

export default {
  name: "Order",
  props: {
    order: {
      type: Object,
      required: true,
    },
  },
  components: {
    OrderItem,
  },
  methods: {
    async cancel(order_id) {
      await this.$store.dispatch("cancelOrder", order_id);
    },
  },
  computed: {
    order_status() {
      if (this.order.status == "P") {
        return "Placed";
      } else if (this.order.status == "S") {
        return "Shipped";
      } else if (this.order.status == "D") {
        return "Delivered";
      } else {
        return "Cancelled";
      }
    },
    total_amount() {
      return this.order.order_items.reduce((total, item) => {
        return total + item.price * item.quantity;
      }, 0);
    },
    address() {
      return this.order.shipping_address;
    },
    created() {
      const [d, m, y] = this.order.created.split("-");
      const date = new Date(d, m - 1, y);
      return date.toDateString();
    },
    cancelled() {
      return this.order.status === "C";
    },
  },
};
</script>

<style scoped>
p {
  margin: 0;
}
.address {
  line-height: 1.2;
}
.click {
  color: #007bff;
}

.click:hover {
  cursor: pointer;
}

.full_name {
  font-size: medium;
  font-weight: 600;
}

.headings div {
  font-size: large;
  font-weight: 700;
  padding: 8px 15px;
}
.card-body {
  padding-bottom: 0;
}
</style>