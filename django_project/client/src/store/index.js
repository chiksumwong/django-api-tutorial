import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);

import createPersistedState from "vuex-persistedstate";

// import Encrypter from "@/helper/encrypter";
// import SecureLS from "secure-ls";
// const ls = new SecureLS({
//   encodingType: "rc4",
//   isCompression: false,
//   encryptionSecret: Encrypter.make_secret(60)
// });

// import Cookies from "js-cookie";

import system from "@/store/modules/system";
import user from "@/store/modules/user";

export const store = new Vuex.Store({
  modules: {
    system,
    user
  },
  plugins: [
    createPersistedState({
      key: "D_S"
    })
    // createPersistedState({
    //   key: "D_S",
    //   storage: {
    //     getItem: key => ls.get(key),
    //     setItem: (key, value) => ls.set(key, value),
    //     removeItem: key => ls.remove(key)
    //   }
    // })
    // createPersistedState({
    //   key: "D_S",
    //   storage: {
    //     getItem: key => Cookies.get(key),
    //     setItem: (key, value) =>
    //       Cookies.set(key, value, { expires: 1 }, { sameSite: "strict" }),
    //     removeItem: key => Cookies.remove(key)
    //   }
    // })
  ]
});
