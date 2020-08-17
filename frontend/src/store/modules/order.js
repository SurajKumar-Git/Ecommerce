import httpClient from "@/AxiosConfig";

export default {
  state: {
    selected_delivery_address: null,
    order_success_message: null,
    orders: [],
  },
  getters: {
    getOrderSuccessMsg(state) {
      return state.order_success_message;
    },
  },
  mutations: {
    setDeliveryAddress(state, address) {
      state.selected_delivery_address = address;
    },
    setOrderSuccessMsg(state) {
      state.order_success_message = "Your order has been placed successfully";
    },
    clearOrderSuccessMsg(state) {
      state.order_success_message = null;
    },
    setOrders(state, orders) {
      state.orders = orders;
    },
    updateStatusCancel(state, order_id) {
      const index = state.orders.findIndex((order) => order.id === order_id);
      console.log(index);
      state.orders[index].status = "C";
      console.log(state.orders[index]);
    },
  },
  actions: {
    async placeOrder({ commit }, order) {
      try {
        await httpClient.post("orders/order/", order);
        commit("clearCartItems");
        commit("setOrderSuccessMsg");
      } catch (error) {
        console.log(error.response.data);
      }
    },
    async fetchOrders({ commit }) {
      try {
        const response = await httpClient.get("orders/order/");
        commit("setOrders", response.data);
      } catch (error) {
        console.log(error.response.data);
      }
    },
    async cancelOrder({ commit }, order_id) {
      try {
        const response = await httpClient.put(`orders/order/${order_id}/`, {
          status: "C",
        });
        commit("updateStatusCancel", order_id, response.data);
      } catch (error) {
        console.log(error.response.data);
      }
    },
  },
};
