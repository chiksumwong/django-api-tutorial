import Vue from "vue";
import App from "./App.vue";
import { i18n } from "./i18n";
import { router } from "./router";
import { store } from "./store";
import "./api";

//Bootstrap
import BootstrapVue from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
Vue.use(BootstrapVue);

//Form Validation
import Vuelidate from "vuelidate";
Vue.use(Vuelidate);

// Vue
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  i18n,
  render: function(h) {
    return h(App);
  }
}).$mount("#app");
