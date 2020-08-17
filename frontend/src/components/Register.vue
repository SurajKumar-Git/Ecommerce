<template>
  <b-modal
    id="register"
    title="Register"
    size="md"
    centered
    header-bg-variant="dark"
    header-text-variant="light"
    :hide-footer="true"
    @show="resetForm"
    @hidden="resetForm"
  >
    <ValidationObserver ref="register" v-slot="{ handleSubmit }">
      <b-form @submit.prevent="handleSubmit(onSubmit)" @reset="resetForm">
        <BTextInputWithValidation
          rules="required|max:32"
          type="text"
          label="First Name"
          name="first_name"
          v-model="first_name"
          placeholder="Enter First Name"
        />
        <BTextInputWithValidation
          rules="required|max:128"
          type="text"
          label="Last Name"
          name="last_name"
          v-model="last_name"
          placeholder="Enter Last Name"
        />
        <BTextInputWithValidation
          rules="required|max:191"
          type="text"
          label="Username"
          name="username"
          v-model="username"
          placeholder="Enter username"
        />
        <BTextInputWithValidation
          rules="required|email|max:254"
          type="email"
          label="Email address"
          name="email"
          v-model="email"
          placeholder="Enter email"
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
        <BTextInputWithValidation
          rules="required|confirmed:Password"
          type="password"
          label="Password confirmation"
          name="confirm_password"
          v-model="confirm_password"
          placeholder="Confirm password"
        />
        <b-button type="reset" variant="outline-dark" class="px-4">Cancel</b-button>
        <b-button type="submit" variant="dark" class="ml-2 px-4">Register</b-button>
      </b-form>
    </ValidationObserver>
    <hr />
    <p>
      Already have an account?
      <span @click="login" class="click">Login</span>
    </p>
  </b-modal>
</template>


<script>
import { ValidationObserver } from "vee-validate";
import BTextInputWithValidation from "@/components/Inputs/BTextInputWithValidation";

export default {
  name: "Register",
  components: {
    ValidationObserver,
    BTextInputWithValidation,
  },
  data() {
    return {
      first_name: "",
      last_name: "",
      username: "",
      email: "",
      password: "",
      confirm_password: "",
    };
  },
  methods: {
    async onSubmit() {
      this.$store.commit("clearRegistrationErrors");
      const user_data = {
        first_name: this.first_name,
        last_name: this.last_name,
        username: this.username,
        email: this.email,
        password: this.password,
      };
      await this.$store.dispatch("userRegistration", user_data);
      const errors = this.$store.state.user.user_registration_errors;
      if (errors != null) {
        this.$refs.register.setErrors(errors);
      } else {
        this.$nextTick(() => {
          this.$bvModal.hide("register");
        });
      }
    },
    resetForm() {
      (this.first_name = ""),
        (this.last_name = ""),
        (this.username = ""),
        (this.email = ""),
        (this.password = ""),
        (this.confirm_password = "");
      if (this.$refs.register) {
        this.$refs.register.reset();
      }
      this.$bvModal.hide("register");
    },
    login() {
      this.$bvModal.hide("register");
      this.$bvModal.show("login");
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