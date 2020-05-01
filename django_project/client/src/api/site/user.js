import Vue from "vue";

const UserAPI = {
  register: payload => Vue.prototype.$axios.post("register/", payload),
  getToken: payload => Vue.prototype.$axios.post("f/auth/token/", payload),
  login: payload => Vue.prototype.$axios.post("f/auth/login/", payload),
  logout: payload => Vue.prototype.$axios.post("f/auth/logout/", payload)
};

export default UserAPI;