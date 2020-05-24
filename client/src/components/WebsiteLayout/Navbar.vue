<template>
  <header class="px-0">
    <!-- Size and Language -->
    <div class="d-none d-md-block d-lg-block d-xl-block container">
      <div class="row justify-content-end">
        <div id="font-size">
          <div
            id="fs-s"
            @click="font('s')"
            :class="[fs_s ? 'font-size-active' : '']"
          >
            A
          </div>
          <div
            id="fs-m"
            @click="font('m')"
            :class="[fs_m ? 'font-size-active' : '']"
          >
            A
          </div>
          <div
            id="fs-l"
            @click="font('l')"
            :class="[fs_l ? 'font-size-active' : '']"
          >
            A
          </div>
        </div>
        <div id="language" class="row">
          <div id="lang-en" v-show="l_en" @click="lang('en')">
            English
          </div>
          <div v-show="l_s1">|</div>
          <div id="lang-tw" v-show="l_tw" @click="lang('tw')">
            繁體
          </div>
          <div v-show="l_s2">|</div>
          <div id="lang-cn" v-show="l_cn" @click="lang('cn')">
            简体
          </div>
        </div>
      </div>
    </div>
    <b-navbar toggleable="md" type="dark" variant="dark">
      <b-container>
        <b-navbar-brand href="/">eShop</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <div class="mx-1 py-1" v-show="!isLogin">
              <b-button
                size="sm"
                class="mr-1"
                variant="success"
                @click="route_to('/login')"
                >Login</b-button
              >
              <b-button size="sm" variant="info" @click="route_to('/register')"
                >Register</b-button
              >
            </div>

            <b-nav-item-dropdown right v-show="isLogin">
              <template v-slot:button-content>
                <em>User</em>
              </template>
              <b-dropdown-item href="#">Profile</b-dropdown-item>
              <b-dropdown-item v-show="isAdmin" @click="route_to('/admin')"
                >Admin Panel</b-dropdown-item
              >
              <b-dropdown-item href="#">Sign Out</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-collapse>
      </b-container>
    </b-navbar>
  </header>
</template>

<script>
export default {
  methods: {
    route_to(path) {
      this.$router.push(path);
    },
    font(size) {
      this.$store.dispatch("system/setFontSize", size);
    },
    lang(lang) {
      this.$store.dispatch("system/setLanguage", lang);
    },
    logout() {
      this.$store.dispatch("user/logout", {
        user_name: this.$store.state.user.n
      });
    }
  },
  computed: {
    isLogin() {
      return this.$store.state.user.l;
    },
    isAdmin() {
      return this.$store.state.user.a;
    },
    fs_s() {
      return this.$store.state.system.fs_s;
    },
    fs_m() {
      return this.$store.state.system.fs_m;
    },
    fs_l() {
      return this.$store.state.system.fs_l;
    },
    l_en() {
      return this.$store.state.system.l_en;
    },
    l_tw() {
      return this.$store.state.system.l_tw;
    },
    l_cn() {
      return this.$store.state.system.l_cn;
    },
    l_s1() {
      return this.$store.state.system.l_s1;
    },
    l_s2() {
      return this.$store.state.system.l_s2;
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
