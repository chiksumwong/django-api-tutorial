import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

// import SecureLS from "secure-ls";
// const ls = new SecureLS({
//   encodingType: "rc4",
//   isCompression: false,
//   encryptionSecret: "s3cs5d4f6sd4!@$a$$w0rd@123"
// });

// import Cookies from "js-cookie";
// const in1Hour = 1 / 12;

import system from "@/store/modules/system";
import user from "@/store/modules/user";

Vue.use(Vuex);

export const store = new Vuex.Store({
  modules: {
    system,
    user
  },
  plugins: [createPersistedState()]
  // plugins: [
  //   createPersistedState({
  //     storage: {
  //       getItem: key => ls.get(key),
  //       setItem: (key, value) => ls.set(key, value),
  //       removeItem: key => ls.remove(key)
  //     }
  //   })
  // ]
  // plugins: [
  //   createPersistedState({
  //     storage: {
  //       getItem: key => Cookies.get(key),
  //       setItem: (key, value) => Cookies.set(key, value, { expires: in1Hour }),
  //       removeItem: key => Cookies.remove(key)
  //     }
  //   })
  // ]
});
