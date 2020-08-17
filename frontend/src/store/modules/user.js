import httpClient from "@/AxiosConfig";

export default {
  state: {
    isAuthenticated:
      JSON.parse(localStorage.getItem("isAuthenticated")) || false,
    user: JSON.parse(localStorage.getItem("user")) || null,
    addresses: [],
    user_registration_errors: null,
  },
  getters: {
    getFullName(state) {
      if (state.user) {
        return `${state.user.first_name} ${state.user.last_name}`;
      }
      return null;
    },
  },
  mutations: {
    deauthenticate(state) {
      state.isAuthenticated = false;
      state.user = {};
    },
    setAuthticated(state) {
      state.isAuthenticated = true;
    },
    setUser(state, user) {
      state.user = user;
    },
    persistUserData(state) {
      localStorage.setItem("isAuthenticated", JSON.stringify(true));
      localStorage.setItem("user", JSON.stringify(state.user));
    },
    removePersistedUserData() {
      localStorage.removeItem("isAuthenticated");
      localStorage.removeItem("user");
    },
    setAddresses(state, addresses) {
      state.addresses = addresses;
    },
    pushNewAddress(state, address) {
      state.addresses.push(address);
    },
    setRegistrationErrors(state, errors) {
      state.user_registration_errors = errors;
    },
    clearRegistrationErrors(state, errors) {
      state.user_registration_errors = errors;
    },
  },
  actions: {
    async fetchUser({ commit }) {
      const response = await httpClient.get("user/");
      commit("setUser", response.data);
      commit("setAuthticated");
      commit("persistUserData");
    },
    async fetchUserAddresses({ commit }) {
      const response = await httpClient.get("user/address/");
      commit("setAddresses", response.data);
    },
    async addNewAddress({ commit }, new_address) {
      const response = await httpClient.post("user/address/", new_address);
      commit("pushNewAddress", response.data);
    },
    async userRegistration({ commit }, user_data) {
      try {
        const response = await httpClient.post("user/register/", user_data);
        const data = response.data;
        const tokens = {
          ...data.tokens,
        };
        commit("updateToken", tokens);

        delete data.tokens;
        const user = {
          ...data,
        };

        commit("setUser", user);
        commit("setAuthticated");
        commit("persistUserData");
      } catch (error) {
        commit("setRegistrationErrors", error.response.data);
      }
    },
  },
};
