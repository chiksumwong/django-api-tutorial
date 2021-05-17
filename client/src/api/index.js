import Vue from "vue";
import { store } from "@/store";
import axios from "axios";

const instance = axios.create({
  baseURL: process.env.VUE_APP_BASE_API,
  headers: {
    "Content-Type": "application/json"
  }
});

instance.interceptors.request.use(
  config => {
    let token = store.state.user.t;
    if (token) {
      const authToken = "Bearer " + token;
      config.headers["Authorization"] = authToken;
    }
    return config;
  },
  error => {
    // return error;
    return Promise.reject(error);
  }
);

instance.interceptors.response.use(
  response => response,
  error => {
    const originalRequest = error.config;
    if (
      error.response.status === 401 &&
      error.response.statusText === "Unauthorized"
    ) {
      // access token -> 向 API 拿新的 token
      const refresh_token = store.state.user.r;
      return axios
        .post(process.env.VUE_APP_BASE_API + "f/auth/token/refresh/", {
          refresh: refresh_token
        })
        .then(response => {
          this.$store.dispatch("user/setToken", {
            access_token: response.data.access
          });
          instance.defaults.headers["Authorization"] =
            "Bearer " + response.data.access;
          originalRequest.headers["Authorization"] =
            "Bearer " + response.data.access;
          return instance(originalRequest);
        })
        .catch(err => {
          // refresh token 過期 -> 直接當作完全沒有登入
          this.$store.dispatch("user/logoutAction");
          console.log(err);
        });
    }
    return Promise.reject(error);
  }
);

Vue.prototype.$axios = instance;
