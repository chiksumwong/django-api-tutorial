import Vue from "vue";

const UserAPI = {
  register: payload => Vue.prototype.$axios.post("/register", payload)
};

export default UserAPI;
