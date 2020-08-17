import httpClient from "@/AxiosConfig";
import inspectToken from "@/store/modules/inspectToken";

export default {
  state: {
    jwt: JSON.parse(localStorage.getItem("token")) || null,
    login_error: null,
    need_authentication: false,
  },
  getters: {
    getAuthHeader(state) {
      if (state.jwt) {
        inspectToken.check_refreshToken();
        return { Authorization: `Bearer ${state.jwt.access}` };
      }
      return {};
    },
  },
  mutations: {
    updateToken(state, { access, refresh }) {
      let newToken = {
        access: null,
        refresh: null,
      };
      if (access && refresh) {
        newToken.access = access;
        newToken.refresh = refresh;
      } else if (access) {
        newToken.access = access;
        newToken.refresh = state.jwt.refresh;
      }
      localStorage.setItem("token", JSON.stringify(newToken));
      state.jwt = newToken;
    },
    removeToken(state) {
      localStorage.removeItem("token");
      state.jwt = null;
    },
    setLoginError(state) {
      state.login_error = { username: ["Invalid credentials"] };
    },
    clearLoginError(state) {
      state.login_error = null;
    },
    setNeedAuthentication(state) {
      state.need_authentication = true;
    },
    clearNeedAuthentication(state) {
      state.need_authentication = false;
    },
  },
  actions: {
    async obtainToken({ commit }, payload) {
      try {
        const response = await httpClient.post("api/token/", payload);
        commit("updateToken", response.data);
        return true;
      } catch {
        commit("setLoginError");
        return false;
      }
    },
    async refreshToken({ commit, state }) {
      const payload = {
        refresh: state.jwt.refresh,
      };
      try {
        const response = await httpClient.post("api/token/refresh/", payload);
        commit("updateToken", response.data);
      } catch (error) {
        console.log(error);
      }
    },
    async login({ dispatch, commit }, payload) {
      commit("clearLoginError");

      if (await dispatch("obtainToken", payload)) {
        await dispatch("fetchUser");
      }
    },
    logout({ commit }) {
      //More about blacklist token and remove token from api
      commit("deauthenticate");
      commit("removeToken");
      commit("removePersistedUserData");
    },
  },
};
