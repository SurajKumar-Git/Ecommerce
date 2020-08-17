import httpClient from "@/AxiosConfig";

export default {
  state: {
    cart_items: [],
  },
  getters: {
    get_cart_items(state) {
      return state.cart_items;
    },
    isCartEmpty(state) {
      return state.cart_items.length == 0;
    },
    isProductInCart(state, getters, rootState) {
      getters;
      const cartitem = state.cart_items.find((item) => {
        return (
          item.product_variant.id === rootState.product.selected_variant.id
        );
      });

      return cartitem !== undefined ? true : false;
    },
    cart_items_total(state) {
      return state.cart_items.reduce((total, item) => {
        return (
          total + item.product_variant.product_inventory.price * item.quantity
        );
      }, 0);
    },
  },
  mutations: {
    addToCartItems(state, data) {
      state.cart_items.push(data);
    },
    setCartItems(state, cart_items) {
      state.cart_items = cart_items;
    },
    removeCartItem(state, cartItem) {
      const cart_items = state.cart_items.filter((item) => {
        return item.id != cartItem.id;
      });
      state.cart_items = cart_items;
    },
    updateCartItem(state, cartItem) {
      const index = state.cart_items.findIndex((item) => {
        return item.id === cartItem.id;
      });
      state.cart_items[index] = cartItem;
    },
    clearCartItems(state) {
      state.cart_items = [];
    },
  },
  actions: {
    async addProductToCart({ commit, rootState }, payload) {
      const response = await httpClient.post("cart/cartitem/", payload);
      const data = {
        ...response.data,
        product_variant: rootState.product.selected_variant,
      };
      const inventory_response = await httpClient.get(
        data.product_variant.product_inventory
      );
      data.product_variant.product_inventory = inventory_response.data;
      commit("addToCartItems", data);
    },
    async fetchCart({ commit }) {
      const response = await httpClient.get("cart/");

      // Fetch Inventory of each item
      const cart_items = response.data.cart_items;
      for (let item of cart_items) {
        const inventory_response = await httpClient.get(
          item.product_variant.product_inventory
        );
        item.product_variant.product_inventory = inventory_response.data;
      }
      commit("setCartItems", cart_items);
    },

    async deleteCartItem({ commit }, cartItem) {
      await httpClient.delete(`cart/cartitem/${cartItem.id}/`);
      commit("removeCartItem", cartItem);
    },
    async changeQuantity({ commit }, cartItem) {
      const payload = {
        product_variant: cartItem.product_variant.id,
        quantity: cartItem.quantity,
      };
      try {
        await httpClient.put(`cart/cartitem/${cartItem.id}/`, payload);
        commit("updateCartItem", cartItem);
        return true;
      } catch (error) {
        return error.response.data;
        //check is needed
      }
    },
  },
};
