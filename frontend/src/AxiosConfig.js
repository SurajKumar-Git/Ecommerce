import axios from "axios";
// import inspectToken from "@/store/modules/inspectToken";

const httpClient = axios.create({
  baseURL: "http://127.0.0.1:5000/",
  timeout: 1000,
  headers: {
    "Content-Type": "application/json",
  },
});

const getAuthToken = () => {
  const jwt = JSON.parse(localStorage.getItem("token"));
  if (jwt) {
    // inspectToken.check_refreshToken();
    return `Bearer ${jwt.access}`;
  }
  return null;
};

const authInterceptor = (config) => {
  config.headers["Authorization"] = getAuthToken();
  return config;
};

httpClient.interceptors.request.use(authInterceptor);

export default httpClient;
