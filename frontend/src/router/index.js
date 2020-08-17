import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import store from "@/store/index";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/product/:product_id",
    name: "Product",
    component: () =>
      import(/* webpackChunkName: "Product" */ "../views/Product"),
  },
  {
    path: "/cart",
    name: "Cart",
    component: () => import(/* webpackChunkName: "Cart" */ "../views/Cart"),
    meta: { requiresAuth: true },
  },
  {
    path: "/cart/select_address",
    name: "SelectAddress",
    component: () =>
      import(/* webpackChunkName: "SelectAddress" */ "../views/AddressSelect"),
    meta: { requiresAuth: true },
  },
  {
    path: "/order",
    name: "Order",
    component: () =>
      import(/* webpackChunkName: "Order" */ "../views/OrderDetail"),
    meta: { requiresAuth: true },
  },
  {
    path: "/my_orders",
    name: "MyOrders",
    component: () =>
      import(/* webpackChunkName: "MyOrders" */ "../views/MyOrders"),
    meta: { requiresAuth: true },
  },
];

const router = new VueRouter({
  routes,
  mode: "history",
});

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth) {
    if (!store.state.user.isAuthenticated) {
      store.commit("setNeedAuthentication");
      next(from);
    }
  } else if (to.meta.requiresAnonymous) {
    if (store.state.user.isAuthenticated) {
      next({ name: "Home" });
    }
  }
  next();
});

export default router;
