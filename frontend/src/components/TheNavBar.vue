<template>
  <div>
    <b-navbar toggleable="lg" variant="dark" type="dark" :sticky="true">
      <b-navbar-brand :to="{name:'Home' }">Right Choice</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <!-- <b-nav-item :to="{ name: 'Categories' }">Category</b-nav-item> -->
          <Category />
        </b-navbar-nav>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="mx-auto w-50">
          <b-nav-form class="w-100" @submit.prevent="search">
            <b-input-group class="w-100">
              <b-form-input size="md" placeholder="Search" v-model="search_input"></b-form-input>
              <b-input-group-append>
                <b-button size="md" class="my-2 my-sm-0" type="submit">Search</b-button>
              </b-input-group-append>
            </b-input-group>
          </b-nav-form>
        </b-navbar-nav>
        <b-navbar-nav>
          <!-- <b-nav-item v-if="!isAutheticated" :to="{ name: 'Login' }">Login</b-nav-item> -->
          <b-nav-item v-if="!isAutheticated" v-b-modal.login @click="ShowLogin">Login</b-nav-item>
          <b-nav-item v-if="!isAutheticated" v-b-modal.register>Register</b-nav-item>
          <b-nav-item v-if="isAutheticated" :to="{ name: 'Cart' }">
            <CartIcon />
          </b-nav-item>
          <b-nav-item-dropdown v-if="isAutheticated" :text="getFullName" right class="text-white">
            <b-dropdown-item :to="{name: 'MyOrders'}">My Orders</b-dropdown-item>
            <b-dropdown-item @click="logout">Logout</b-dropdown-item>
          </b-nav-item-dropdown>

          <!-- <b-nav-item v-if="isAutheticated" @click="logout">Logout</b-nav-item> -->
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <Register />
    <Login />
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import CartIcon from "@/components/CartIcon";
import Register from "@/components/Register";
import Login from "@/components/Login";
import Category from "@/components/Category";

export default {
  name: "TheNavBar",
  components: {
    CartIcon,
    Register,
    Login,
    Category,
  },
  data() {
    return {
      search_input: "",
    };
  },
  computed: {
    ...mapGetters(["getFullName"]),
    isAutheticated() {
      return this.$store.state.user.isAuthenticated;
    },
  },
  methods: {
    logout() {
      this.$store.dispatch("logout");
      this.$router.push({ name: "Home" });
    },
    search() {
      const params = {
        search: this.search_input,
      };
      this.$store.dispatch("fetchProducts", params);
      this.search_input = "";
    },
    ShowLogin() {
      this.$bvModal.show("login");
    },
  },
};
</script>

<style>
form {
  width: 100%;
}

.navbar-dark .navbar-nav .nav-link {
  color: white !important;
}
</style>
