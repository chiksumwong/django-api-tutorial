import Vue from "vue";
import { router } from "@/router";
import axios from "axios";
import Cookies from "js-cookie";

const instance = axios.create({
  baseURL: process.env.VUE_APP_BASE_API,
  headers: {
    "Content-Type": "application/json"
  }
});

instance.interceptors.request.use(
  config => {
    let token = Cookies.get("t");
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

instance.interceptors.response.use(
  response => {
    console.log("response: ", response.data);
    return response;
  },
  error => {
    const originalRequest = error.config;
    console.log("originalRequest: ", originalRequest);
    if (
      error.response.status === 401 &&
      originalRequest.url === process.env.VUE_APP_BASE_API + "f/auth/token/"
    ) {
      router.push("/login");
      return Promise.reject(error);
    }

    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      const refreshToken = Cookies.get("r");
      return axios
        .post("f/auth/token/refresh/", {
          refresh: refreshToken
        })
        .then(res => {
          if (res.status === 201) {
            // Save Token
            Cookies.set(
              "t",
              res.data.access,
              { expires: 1 / 12 },
              { sameSite: "strict" }
            );
            // // Save refresh Token
            // Cookies.set(
            //   "r",
            //   res.data.refresh,
            //   { expires: 1 },
            //   { sameSite: "strict" }
            // );
            axios.defaults.headers.common["Authorization"] =
              "Bearer " + Cookies.get("t");
            return axios(originalRequest);
          }
        });
    }
    return Promise.reject(error);
  }
);

Vue.prototype.$axios = instance;
