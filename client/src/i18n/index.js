import Vue from "vue";
import { store } from "@/store";
import VueI18n from "vue-i18n";
Vue.use(VueI18n);

import en from "./en/lang";
import tw from "./zh-TW/lang";
import cn from "./zh-CN/lang";

const locale = store.state.system.l || "tw";

export const i18n = new VueI18n({
  locale,
  messages: { en, tw, cn }
});
