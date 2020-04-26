import { router } from "@/router";
import UserAPI from "@/api/user";
const jwtDecode = require("jwt-decode");
import Cookies from "js-cookie";

export default {
  namespaced: true,
  state: {
    n: null, //user name
    i: null, //id
    l: false, // is login
    a: false // is admin
  },
  actions: {
    async login({ commit }, payload) {
      try {
        const user = {};

        // Get Token
        const res1 = await UserAPI.getToken(payload);
        if (res1.data) {
          user.token = res1.data.access;
        } else {
          console.log("Fail", res1.err);
        }

        // Save Token
        Cookies.set(
          "t",
          res1.data.access,
          { expires: 1 / 12 },
          { sameSite: "strict" }
        );

        // Save refresh Token
        Cookies.set(
          "r",
          res1.data.refresh,
          { expires: 1 },
          { sameSite: "strict" }
        );

        // Decoded
        var decoded = jwtDecode(res1.data.access);
        console.log("decoded", decoded);

        // Get User Info
        const res2 = await UserAPI.login({ user_id: decoded.user_id });
        if (res2.data) {
          user.id = decoded.user_id;
          user.name = res2.data.username;
          user.isAdmin = res2.data.is_staff;
        } else {
          console.log("Fail", res2.err);
        }

        // Commit State
        commit("loginSuccess", user);

        // Redirect
        router.push("/");
      } catch (e) {
        commit("loginFailure");
        router.push("/login");
      }
    },
    async logout({ commit }, payload) {
      const res = await UserAPI.logout(payload);
      console.log("res: ", res);
      if (res.data) {
        console.log("Success", res.data);
      } else {
        console.log("Fail", res.err);
      }
      Cookies.remove("t");
      commit("logout");
      router.push("/");
    },
    logoutAction({ commit }) {
      Cookies.remove("t");
      commit("logout");
      router.push("/");
    }
  },
  mutations: {
    loginSuccess(state, user) {
      state.n = user.name;
      state.i = user.id;
      state.l = true;
      state.a = user.isAdmin;
    },
    loginFailure(state) {
      state.n = null;
      state.i = null;
      state.l = false;
      state.a = false;
    },
    logout(state) {
      state.n = null;
      state.i = null;
      state.l = false;
      state.a = false;
    }
  }
};
