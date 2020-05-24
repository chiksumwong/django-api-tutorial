import { i18n } from "@/i18n";

export default {
  namespaced: true,
  state: {
    fs: "m", // Font Size
    fs_s: false,
    fs_m: true,
    fs_l: false,
    l: "tw", // Language
    l_en: true,
    l_tw: false,
    l_cn: true,
    l_s1: true,
    l_s2: false
  },
  actions: {
    setLanguage({ commit }, lang) {
      if (lang === "en") {
        commit("switchEN");
        i18n.locale = "en";
      } else if (lang === "cn") {
        commit("switchCN");
        i18n.locale = "cn";
      } else {
        commit("switchTW");
        i18n.locale = "tw";
      }
    },
    setFontSize({ commit }, size) {
      if (size === "s") {
        commit("switchFS");
        document.querySelector("html").style.fontSize = "12px";
      } else if (size === "l") {
        commit("switchFL");
        document.querySelector("html").style.fontSize = "17px";
      } else {
        commit("switchFM");
        document.querySelector("html").style.fontSize = "15px";
      }
    }
  },
  mutations: {
    switchFS(state) {
      state.fs_s = true;
      state.fs_m = false;
      state.fs_l = false;
      state.fs_l = false;
      state.fs = "s";
    },
    switchFM(state) {
      state.fs_s = false;
      state.fs_m = true;
      state.fs_l = false;
      state.fs = "m";
    },
    switchFL(state) {
      state.fs_s = false;
      state.fs_m = false;
      state.fs_l = true;
      state.fs = "l";
    },
    switchTW(state) {
      state.l_en = true;
      state.l_tw = false;
      state.l_cn = true;
      state.l_s1 = false;
      state.l_s2 = true;
      state.l = "tw";
    },
    switchCN(state) {
      state.l_en = true;
      state.l_tw = true;
      state.l_cn = false;
      state.l_s1 = true;
      state.l_s2 = false;
      state.l = "cn";
    },
    switchEN(state) {
      state.l_en = false;
      state.l_tw = true;
      state.l_cn = true;
      state.l_s1 = false;
      state.l_s2 = true;
      state.l = "en";
    }
  }
};
