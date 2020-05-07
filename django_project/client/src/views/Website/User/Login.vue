<template>
  <b-container>
    <div class="mx-auto col-sm-6 mt-5">
      <div class="form-title">Login</div>
      <b-form
        style="border-style: solid;border-color: #343a40;"
        class="p-3"
        @submit.prevent="handleSubmit"
      >
        <!-- username -->
        <b-row class="mt-1">
          <b-col sm="3">
            <label class="form-label">User Name</label>
          </b-col>
          <b-col sm="9">
            <b-form-input
              size="sm"
              v-model="form.username"
              :class="{ 'is-invalid': submitted && $v.form.username.$error }"
            ></b-form-input>
            <div
              v-if="submitted && $v.form.username.$error"
              class="invalid-feedback"
            >
              <span v-if="!$v.form.username.required"
                >User name is required</span
              >
            </div>
          </b-col>
        </b-row>

        <!-- password -->
        <b-row class="mt-1">
          <b-col sm="3">
            <label class="form-label">Password</label>
          </b-col>
          <b-col sm="9">
            <b-form-input
              size="sm"
              v-model="form.password"
              type="password"
              aria-describedby="password-help-block"
              :class="{ 'is-invalid': submitted && $v.form.password.$error }"
            ></b-form-input>
            <div
              v-if="submitted && $v.form.password.$error"
              class="invalid-feedback"
            >
              <span v-if="!$v.form.password.required"
                >Password is required</span
              >
            </div>
          </b-col>
        </b-row>

        <!-- button -->
        <b-row class="justify-content-end">
          <b-button
            squared
            size="sm"
            class="my-2 mx-3 button-item"
            @click="handleSubmit()"
            >Login</b-button
          >
        </b-row>
        <!-- <router-link to="/register"> Register </router-link><br />
        <router-link to="/forgot_password">Forgot Password</router-link> -->

        <!-- Google Sign-in -->
        <!-- <b-button id="googleSignIn" size="sm" @click="loginWithGoogle()"
          >Google Sign In</b-button
        >
        <b-button squared size="sm" @click="logoutWithGoogle()"
          >Google Sign Out</b-button
        > -->
        <!-- Facebook Sign-in -->
        <!-- <b-button @click="loginWithFacebook()">Login with Facebook</b-button>
        <b-button @click="logoutWithFacebook()">Logout with Facebook</b-button>
        <b-button @click="getFacebookProfile()">getFacebookProfile</b-button> -->
        <div class="text-center">
          <!-- Google and Facebook Login Button -->
          <button
            class="loginBtn loginBtn--google"
            id="googleSignIn"
            @click="loginWithGoogle()"
          >
            Login with Google
          </button>
          <button
            class="loginBtn loginBtn--facebook"
            @click="loginWithFacebook()"
          >
            Login with Facebook
          </button>
        </div>
      </b-form>
    </div>
  </b-container>
</template>

<script>
import { required } from "vuelidate/lib/validators";
export default {
  data() {
    return {
      form: {
        username: "",
        password: ""
      },
      submitted: false
    };
  },
  validations: {
    form: {
      username: {
        required
      },
      password: {
        required
      }
    }
  },
  methods: {
    handleSubmit() {
      this.submitted = true;

      // stop here if form is invalid
      this.$v.$touch();
      if (this.$v.$invalid) {
        return;
      }

      const username = this.form.username;
      const password = this.form.password;
      if (username && password) {
        this.$store.dispatch("user/login", {
          username,
          password
        });
      }
    },
    // Google
    loginWithGoogle() {
      let auth2 = window.gapi.auth2.getAuthInstance();
      auth2.attachClickHandler(
        "googleSignIn",
        {},
        function(googleUser) {
          console.log(googleUser.getBasicProfile());
        },
        function(error) {
          alert(JSON.stringify(error, undefined, 2));
        }
      );
    },
    logoutWithGoogle() {
      let auth2 = window.gapi.auth2.getAuthInstance();
      auth2.signOut().then(function() {
        console.log("User signed out.");
      });
    },
    initGoogle() {
      window.gapi.load("auth2", function() {
        window.gapi.auth2.init({
          client_id: process.env.VUE_APP_GOOGLE_CLIENT_ID,
          cookiepolicy: "single_host_origin",
          scope: "profile email"
        });
      });
    },
    // Facebook
    loginWithFacebook() {
      const vm = this;
      window.FB.getLoginStatus(function(response) {
        if (response.status === "connected") {
          vm.getFacebookProfile();
        } else {
          window.FB.login(
            function(response) {
              if (response.authResponse) {
                vm.getFacebookProfile();
              } else {
                alert("User cancelled login or did not fully authorize.");
              }
            },
            { scope: "public_profile,email" }
          );
        }
      });
    },
    logoutWithFacebook() {
      window.FB.getLoginStatus(function(response) {
        // 檢查登入狀態
        if (response.status === "connected") {
          window.FB.logout(function(response) {
            console.log("Logout: ", response);
          });
        } else {
          // do something
        }
      });
    },
    getFacebookProfile() {
      window.FB.api("/me", function(res) {
        console.log(res);
      });
    },
    initFacebook() {
      window.fbAsyncInit = function() {
        window.FB.init({
          appId: process.env.VUE_APP_FACEBOOK_APP_ID,
          cookie: true,
          xfbml: true,
          version: process.env.VUE_APP_FACEBOOK_API_VERSION
        });
        window.FB.AppEvents.logPageView();
      };
    },
    loadFacebookSDK(d, s, id) {
      var js,
        fjs = d.getElementsByTagName(s)[0];
      if (d.getElementById(id)) {
        return;
      }
      js = d.createElement(s);
      js.id = id;
      js.src = "https://connect.facebook.net/en_US/sdk.js";
      fjs.parentNode.insertBefore(js, fjs);
    }
  },
  mounted() {
    this.initGoogle();
    if (!window.FB) {
      this.loadFacebookSDK(document, "script", "facebook-jssdk");
      this.initFacebook();
    }
  }
};
</script>

<style scoped>
.form-title {
  font-size: 1.5em;
  background: #343a40;
  color: #f8f9fa;
  font-weight: bold;
  height: 40px;
  padding-left: 10px;
}
.form-label {
  border-collapse: separate;
  border-spacing: 3px;
  font: inherit;
  vertical-align: top;
  font-size: 0.9em;
  margin: 0px;
  color: #343a40;
  padding: 4px 3px;
  font-weight: bold;
}
.button-item {
  background-color: #343a40;
}

.loginBtn {
  box-sizing: border-box;
  position: relative;
  width: 13em;
  margin: 0.2em;
  padding: 0 15px 0 46px;
  border: none;
  text-align: left;
  line-height: 34px;
  white-space: nowrap;
  border-radius: 0.2em;
  font-size: 16px;
  color: #fff;
}
.loginBtn:before {
  content: "";
  box-sizing: border-box;
  position: absolute;
  top: 0;
  left: 0;
  width: 34px;
  height: 100%;
}
.loginBtn:focus {
  outline: none;
}
.loginBtn:active {
  box-shadow: inset 0 0 0 32px rgba(0, 0, 0, 0.1);
}

/* Google */
.loginBtn--google {
  /*font-family: "Roboto", Roboto, arial, sans-serif;*/
  background: #dd4b39;
}
.loginBtn--google:before {
  border-right: #bb3f30 1px solid;
  background: url("https://s3-us-west-2.amazonaws.com/s.cdpn.io/14082/icon_google.png")
    6px 6px no-repeat;
}
.loginBtn--google:hover,
.loginBtn--google:focus {
  background: #e74b37;
}

/* Facebook */
.loginBtn--facebook {
  background-color: #4c69ba;
  background-image: linear-gradient(#4c69ba, #3b55a0);
  /*font-family: "Helvetica neue", Helvetica Neue, Helvetica, Arial, sans-serif;*/
  text-shadow: 0 -1px 0 #354c8c;
}
.loginBtn--facebook:before {
  border-right: #364e92 1px solid;
  background: url("https://s3-us-west-2.amazonaws.com/s.cdpn.io/14082/icon_facebook.png")
    6px 6px no-repeat;
}
.loginBtn--facebook:hover,
.loginBtn--facebook:focus {
  background-color: #5b7bd5;
  background-image: linear-gradient(#5b7bd5, #4864b1);
}
</style>
