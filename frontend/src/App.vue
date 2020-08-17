<template>
  <div id="app" class="d-flex flex-column">
    <TheNavBar />
    <router-view class="mb-5 flex-fill" />
    <TheFooter />
  </div>
</template>

<script>
import TheNavBar from "@/components/TheNavBar";
import TheFooter from "@/components/TheFooter";

export default {
  name: "App",
  components: {
    TheNavBar,
    TheFooter,
  },
  async created() {
    if (this.$store.state.user.isAuthenticated) {
      await this.$store.dispatch("fetchCart");
    }
  },
};
</script>

<style>
body {
  background-color: #fafcff;
}

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  font-family: "Raleway", sans-serif;
  min-height: 100vh;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
