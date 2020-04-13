import Vue from "vue";
import Vuex from "vuex";
// import PersistedState from "vuex-persistedstate";

// import system from "@/store/modules/system";
// import user from "@/store/modules/user";

Vue.use(Vuex);

export const store = new Vuex.Store({
  modules: {
    // system,
    // user
  },
  // plugins: [PersistedState()]
});
