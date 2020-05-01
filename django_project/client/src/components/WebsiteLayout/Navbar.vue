<template>
  <header>
    <div class="container">
      <b-navbar toggleable="md" class="pl-0 ">
        <!-- Icon -->
        <div v-show="isAdmin">
          <b-navbar-brand
            class="d-none d-md-block d-lg-block d-xl-block"
            @click="route_to('/dashboard')"
          >
            Shop
          </b-navbar-brand>
        </div>
        <div v-show="!isAdmin">
          <b-navbar-brand
            class="d-none d-md-block d-lg-block d-xl-block"
            @click="route_to('/')"
          >
            Shop
          </b-navbar-brand>
        </div>
        <!-- Icon - Mobile -->
        <div class="d-sm-block d-md-none">
          <h1 class="name">Shop</h1>
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
          <!-- System Name -->
          <div class="col-sm-12 d-none d-md-block d-lg-block d-xl-block">
            <div class="row justify-content-end">
              <h1 class="name">Django API Tutorila</h1>
            </div>
          </div>
          <!-- Links -->
          <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav class="ml-auto">
              <!-- Product -->
              <b-nav-item v-show="!isLogin">
                <router-link to="/products">
                  <div class="nav-item">
                    Products
                  </div>
                </router-link>
              </b-nav-item>
              <!-- Create Application -->
              <!-- <b-nav-item v-show="!isLogin">
                <router-link to="/application/create">
                  <div class="nav-item">
                    Create Application
                  </div>
                </router-link>
              </b-nav-item> -->
              <!-- Login -->
              <b-nav-item v-show="!isLogin">
                <router-link to="/login">
                  <div class="nav-item">
                    Login
                  </div>
                </router-link>
              </b-nav-item>
              <!-- Registration -->
              <b-nav-item v-show="!isLogin">
                <router-link to="/register">
                  <div class="nav-item">
                    Registration
                  </div>
                </router-link>
              </b-nav-item>
              <!-- Drapdown - Admin -->
              <b-nav-item-dropdown text="Admin" right>
                <b-dropdown-item @click="route_to('/system_logs')"
                  >System Log</b-dropdown-item
                >
                <b-dropdown-item @click="route_to('/applications')"
                  >Application</b-dropdown-item
                >
                <b-dropdown-item @click="route_to('/product/create')"
                  >Create Products</b-dropdown-item
                >
                <b-dropdown-item @click="route_to('/files')"
                  >Files</b-dropdown-item
                >
              </b-nav-item-dropdown>
              <!-- End - Drapdown - Admin -->
            </b-navbar-nav>
          </b-collapse>
        </div>
      </b-navbar>
    </div>
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
      // return this.$store.state.user.status.isLogin;
      return false;
    },
    isAdmin() {
      // return this.$store.state.user.isAdmin;
      return false;
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
