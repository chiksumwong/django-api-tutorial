import Vue from "vue";
import App from "./App.vue";
import { router } from "./router";
import { store } from "./store";

//Bootstrap
import BootstrapVue from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
Vue.use(BootstrapVue);

//Form Validation
import Vuelidate from "vuelidate";
Vue.use(Vuelidate);

//i18n
import VueI18n from "vue-i18n";
import en from "./i18n/en/lang";
import tw from "./i18n/zh-TW/lang";
import cn from "./i18n/zh-CN/lang";
Vue.use(VueI18n);
const locale = localStorage.getItem("locale") || "tw";
const i18n = new VueI18n({
  locale,
  messages: { en, tw, cn }
});

// Axios
import axios from 'axios'
const instance  = axios.create({
  // baseURL: (process.env.VUE_APP_BASE_URL !== undefined) ? process.env.VUE_APP_BASE_URL : 'http://localhost:3000/api/v1/'
  // baseURL: process.env.VUE_APP_BASE_API,
  baseURL: "http://127.0.0.1:8000/api/"
})
// instance.interceptors.request.use(
//  (config) => {
//    let token = localStorage.getItem('token');

//    if (token) {
//      const authToken = 'Bearer ' + token
//      config.headers['Authorization'] = authToken
//    }

//    return config
//  },
//  (error) => {
//    return Promise.reject(error)
//  }
// )
Vue.prototype.$axios = instance ;

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  i18n,
  render: function(h) {
    return h(App);
  }
}).$mount("#app");
