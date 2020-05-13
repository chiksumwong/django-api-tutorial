import { router } from "@/router";
import UserAPI from "@/api/site/user";
const jwtDecode = require("jwt-decode");

export default {
  namespaced: true,
  state: {
    n: null, //user name
    i: null, //id
    l: false, // is login
    a: false, // is admin
    t: null, // access token
    r: null // refresh token
  },
  actions: {
    async login({ commit }, payload) {
      try {
        // Decoded
        var decoded = jwtDecode(payload.token);
        // Get User Info
        const res = await UserAPI.login({ user_id: decoded.user_id });
        if (res.data) {
          const user = {};
          user.id = decoded.user_id;
          user.name = res.data.username;
          user.isAdmin = res.data.is_staff;
          user.token = payload.token;
          // Commit State
          commit("loginSuccess", user);
          // Redirect
          router.push("/");
        }
      } catch (e) {
        commit("loginFailure");
      }
    },
    async logout({ commit }, payload) {
      await UserAPI.logout(payload);
      commit("logout");
      router.push("/");
    },
    logoutAction({ commit }) {
      commit("logout");
    },
    setToken({ commit }, payload) {
      commit("setToken", payload);
    }
  },
  mutations: {
    loginSuccess(state, user) {
      state.n = user.name;
      state.i = user.id;
      state.l = true;
      state.a = user.isAdmin;
      state.t = user.token;
      state.r = user.r_token;
    },
    loginFailure(state) {
      state.n = null;
      state.i = null;
      state.l = false;
      state.a = false;
      state.t = null;
      state.r = null;
    },
    logout(state) {
      state.n = null;
      state.i = null;
      state.l = false;
      state.a = false;
      state.t = null;
      state.r = null;
    },
    setToken(state, payload) {
      state.t = payload.access_token;
    }
  }
};
