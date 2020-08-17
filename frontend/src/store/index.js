import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

import product from "./modules/product";
import authentication from "./modules/authentication";
import user from "./modules/user";
import cart from "./modules/cart";
import order from "./modules/order";
import rating_review from "./modules/rating_review";

export default new Vuex.Store({
  state: {},
  getters: {
    getFullUrl() {
      return (url) => {
        return "http://127.0.0.1:5000".concat(url);
      };
    },
  },
  mutations: {},
  actions: {},
  modules: {
    product,
    authentication,
    user,
    cart,
    order,
    rating_review,
  },
});
