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
  response => {
    return response;
  },
  error => {
    //handle 401
    if (error.response && error.response.status === 401) {
      store.dispatch("user/logoutAction");
    }
    return error;
    // return Promise.reject(error);
  }
);

Vue.prototype.$axios = instance;
