// import UserAPI from "@/api/user";
import { router } from "@/router";

export default {
  namespaced: true,
  state: {
    n: null, //user name
    i: null, //id
    t: null, //token
    l: false, // is login
    a: false // is admin
  },
  actions: {
    async login({ commit }, payload) {
      try {
        console.log("payload", payload);
        // user login via user login api, get all data
        // const res = await UserAPI.login(payload);
        // console.log("login success", res.data);
        let fake_data = {
          user_name: "fake name", //user name
          user_id: null, //id
          token: "301DvypxO4142vMXsi5IIhWcIPRxly", //token
          isAdmin: false // is admin
        };
        commit("loginSuccess", fake_data);
        // router.push("/");
      } catch (e) {
        console.log(e);
        commit("loginFailure");
        router.push("/login");
      }
    },
    logout({ commit }) {
      commit("logout");
      router.push("/");
    }
  },
  mutations: {
    loginSuccess(state, user) {
      state.u = user.user_name;
      state.i = user.user_id;
      state.t = user.token;
      state.l = true;
      state.a = user.isAdmin;
    },
    loginFailure(state) {
      state.u = null;
      state.i = null;
      state.t = null;
      state.l = false;
      state.a = false;
    },
    logout(state) {
      state.u = null;
      state.i = null;
      state.t = null;
      state.l = false;
      state.a = false;
    }
  }
};
