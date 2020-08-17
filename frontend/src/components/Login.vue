<template>
  <b-modal
    id="login"
    title="Login"
    size="md"
    centered
    header-bg-variant="dark"
    header-text-variant="light"
    :hide-footer="true"
    @show="resetForm"
    @hidden="resetForm"
    v-model="showLogin"
  >
    <ValidationObserver ref="login" v-slot="{ handleSubmit }">
      <b-form @submit.prevent="handleSubmit(onSubmit)" @reset="resetForm">
        <BTextInputWithValidation
          rules="required|max:191"
          type="text"
          label="Username"
          name="username"
          v-model="username"
          placeholder="Enter username"
        />
        <BTextInputWithValidation
          rules="required|min:8"
          type="password"
          label="Password"
          vid="Password"
          name="password"
          v-model="password"
          placeholder="Enter Password"
        />
        <p class="click">Forgot Password?</p>
        <b-button type="submit" variant="dark" class="px-5">Login</b-button>
      </b-form>
    </ValidationObserver>
    <hr />
    <p>
      Don't have an account?
      <span @click="register" class="click">Register</span>
    </p>
  </b-modal>
</template>

<script>
import { ValidationObserver } from "vee-validate";
import BTextInputWithValidation from "@/components/Inputs/BTextInputWithValidation";

export default {
  name: "login",
  components: {
    ValidationObserver,
    BTextInputWithValidation,
  },
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    async onSubmit() {
      const data = {
        username: this.username,
        password: this.password,
      };
      await this.$store.dispatch("login", data);
      const errors = this.$store.state.authentication.login_error;
      if (errors != null) {
        this.$refs.login.setErrors(errors);
      } else {
        this.resetForm();
      }
    },
    resetForm() {
      this.$bvModal.hide("login");
      this.$store.commit("clearNeedAuthentication");
      this.username = "";
      this.password = "";
    },
    register() {
      this.$bvModal.hide("login");
      this.$bvModal.show("register");
    },
  },
  computed: {
    showLogin: {
      get: function () {
        return this.$store.state.authentication.need_authentication;
      },
      set: function () {
        this.$store.commit("setNeedAuthentication");
      },
    },
  },
};
</script>

<style scoped>
.click {
  color: #007bff;
}

.click:hover {
  cursor: pointer;
}
</style>