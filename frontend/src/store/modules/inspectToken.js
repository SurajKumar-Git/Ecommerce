import store from "@/store/index";
import router from "@/router/index";
import jwt_decode from "jwt-decode";

export default {
  check_refreshToken: () => {
    const { exp: access_exp } = jwt_decode(
      store.state.authentication.jwt.access
    );
    const { exp: refresh_exp } = jwt_decode(
      store.state.authentication.jwt.refresh
    );
    const current_time = Date.now().valueOf() / 1000;
    if (
      access_exp - current_time > 0 &&
      access_exp - current_time < 900 &&
      refresh_exp - current_time > 3600
    ) {
      store.dispatch("refreshToken");
    } else if (access_exp - current_time < 0) {
      store.dispatch("logout");
      router.push({ name: "Login" });
    }
  },
};
