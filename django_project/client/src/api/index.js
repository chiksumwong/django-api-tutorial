import Vue from "vue";
import { store } from "@/store";
import axios from "axios";

const instance = axios.create({
  // baseURL: (process.env.VUE_APP_BASE_URL !== undefined) ? process.env.VUE_APP_BASE_URL : 'http://localhost:3000/api/v1/'
  // baseURL: process.env.VUE_APP_BASE_API,
  baseURL: "http://127.0.0.1:8000/api/",
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
    return Promise.reject(error);
  }
);

Vue.prototype.$axios = instance;
