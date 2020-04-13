<template>
  <header>
    <div class="container">
      <b-navbar toggleable="md" class="pl-0 ">
        <!-- Icon -->
        <!-- <div v-show="isAdmin">
          <b-navbar-brand
            class="d-none d-md-block d-lg-block d-xl-block"
            @click="route_to('/dashboard')"
          >
            Django API Tutorila
          </b-navbar-brand>
        </div>
        <div v-show="!isAdmin">
          <b-navbar-brand
            class="d-none d-md-block d-lg-block d-xl-block"
            @click="route_to('/')"
          >
             Django API Tutorila
          </b-navbar-brand>
        </div> -->
        <!-- Icon - Mobile -->
        <div class="d-sm-block d-md-none">
          <h1 class="name">Django API Tutorila</h1>
        </div>

        <!-- Toggle -->
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <!-- Left Side -->
        <div class="row ml-auto w-100">
          <!-- Size and Language -->
          <div class="col-sm-12 d-none d-md-block d-lg-block d-xl-block">
            <div class="row justify-content-end">
              <div id="font-size">
                <div
                  id="fs-s"
                  @click="font_small()"
                  :class="[fs_s ? 'font-size-active' : '']"
                >
                  A
                </div>
                <div
                  id="fs-m"
                  @click="font_middle()"
                  :class="[fs_m ? 'font-size-active' : '']"
                >
                  A
                </div>
                <div
                  id="fs-l"
                  @click="font_large()"
                  :class="[fs_l ? 'font-size-active' : '']"
                >
                  A
                </div>
              </div>
              <div id="language" class="row">
                <div id="lang-en" v-show="lang_en" @click="switch_en()">
                  English
                </div>
                <div v-show="lang_s1">|</div>
                <div id="lang-tw" v-show="lang_tw" @click="switch_tw()">
                  繁體
                </div>
                <div v-show="lang_s2">|</div>
                <div id="lang-cn" v-show="lang_cn" @click="switch_cn()">
                  简体
                </div>
              </div>
            </div>
          </div>
          <!-- System Name -->
          <div class="col-sm-12 d-none d-md-block d-lg-block d-xl-block">
            <div class="row justify-content-end">
              <h1 class="name">Django API Tutorila</h1>
            </div>
          </div>
          <!-- Links -->
          <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav class="ml-auto">
              <!-- Login -->
              <b-nav-item v-show="!isLogin">
                <router-link to="/login">
                  <div class="nav-item">
                    {{ $t("nav.login") }}
                  </div>
                </router-link>
              </b-nav-item>
            </b-navbar-nav>
          </b-collapse>
        </div>
      </b-navbar>
    </div>
  </header>
</template>

<script>
export default {
  data() {
    return {
      fs_s: false,
      fs_m: true,
      fs_l: false,
      lang_en: true,
      lang_tw: false,
      lang_cn: true,
      lang_s1: true,
      lang_s2: false,
    };
  },
  mounted() {
    let size = localStorage.getItem("size");
    if (size === "s") {
      this.font_small();
    } else if (size === "m") {
      this.font_middle();
    } else if (size === "l") {
      this.font_large();
    } else {
      this.font_middle();
      localStorage.setItem("size", "m");
    }
    let lang = localStorage.getItem("locale");
    if (lang === "tw") {
      this.switch_tw();
      this.$store.dispatch("system/switchLang", "tw");
    } else if (lang === "en") {
      this.switch_en();
      this.$store.dispatch("system/switchLang", "en");
    } else if (lang === "cn") {
      this.switch_cn();
      this.$store.dispatch("system/switchLang", "cn");
    } else {
      this.switch_tw;
      localStorage.setItem("locale", "tw");
    }
  },
  methods: {
    route_to(path) {
      this.$router.push(path);
    },
    font_small() {
      this.fs_s = false;
      this.fs_m = false;
      this.fs_l = false;
      this.fs_s = true;
      document.querySelector("html").style.fontSize = "12px";
      localStorage.setItem("size", "s");
    },
    font_middle() {
      this.fs_s = false;
      this.fs_m = false;
      this.fs_l = false;
      this.fs_m = true;
      document.querySelector("html").style.fontSize = "15px";
      localStorage.setItem("size", "m");
    },
    font_large() {
      this.fs_s = false;
      this.fs_m = false;
      this.fs_l = false;
      this.fs_l = true;
      document.querySelector("html").style.fontSize = "17px";
      localStorage.setItem("size", "l");
    },
    switch_en() {
      this.lang_en = false;
      this.lang_tw = false;
      this.lang_cn = false;
      this.lang_s1 = false;
      this.lang_s2 = false;
      this.lang_tw = true;
      this.lang_s2 = true;
      this.lang_cn = true;
      this.switchLang("en");
      localStorage.setItem("locale", "en");
      this.$store.dispatch("system/switchLang", "en");
    },
    switch_tw() {
      this.lang_en = false;
      this.lang_tw = false;
      this.lang_cn = false;
      this.lang_s1 = false;
      this.lang_s2 = false;
      this.lang_en = true;
      this.lang_s2 = true;
      this.lang_cn = true;
      this.switchLang("tw");
      localStorage.setItem("locale", "tw");
      this.$store.dispatch("system/switchLang", "tw");
    },
    switch_cn() {
      this.lang_en = false;
      this.lang_tw = false;
      this.lang_cn = false;
      this.lang_s1 = false;
      this.lang_s2 = false;
      this.lang_en = true;
      this.lang_s1 = true;
      this.lang_tw = true;
      this.switchLang("cn");
      localStorage.setItem("locale", "cn");
      this.$store.dispatch("system/switchLang", "cn");
    },
    switchLang(lang) {
      this.$i18n.locale = lang;
      localStorage.setItem("locale", lang);
    },
    // logout() {
    //   this.$store.dispatch("user/logout");
    // }
  },
  computed: {
    isLogin() {
      // return this.$store.state.user.status.isLogin;
      return false;
    },
    isAdmin() {
      // return this.$store.state.user.isAdmin;
      return false;
    }
  }
};
</script>

<style scoped>
.nav-item {
  text-align: center;
  color: #004775;
}
.name {
  color: #0069ae;
}
.button-item {
  background-color: #036ab5;
}
#font-size {
  display: inline-block;
  border-right: 1px solid #b5b5b5;
}
#fs-s {
  font-size: 12px;
  display: inline-block;
  margin: 0 4px;
}
#fs-m {
  font-size: 16px;
  display: inline-block;
  margin: 0 4px;
}
#fs-l {
  font-size: 20px;
  display: inline-block;
  margin: 0 4px;
}
#fs-s:hover {
  font-weight: bold;
  text-decoration: underline;
  cursor: pointer;
}
#fs-m:hover {
  font-weight: bold;
  text-decoration: underline;
  cursor: pointer;
}
#fs-l:hover {
  font-weight: bold;
  text-decoration: underline;
  cursor: pointer;
}
.font-size-active {
  font-weight: bold;
  text-decoration: underline;
}
#language {
  margin: 0px 2px;
  font-size: 1.3em;
  font-family: "微軟正黑體", "Microsoft JhengHei";
}
#lang-en:hover {
  text-decoration: underline;
  cursor: pointer;
}
#lang-tw:hover {
  text-decoration: underline;
  cursor: pointer;
}
#lang-cn:hover {
  text-decoration: underline;
  cursor: pointer;
}
</style>
