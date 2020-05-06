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
        <div id="google-signin-button"></div>
        <b-button squared size="sm" class="button-item" @click="signOut()"
          >Google Sign Out</b-button
        >
        <!-- Facebook Sign-in -->
        <b-button @click="logInWithFacebook()">Login with Facebook</b-button>
        <b-button @click="logoutWithFacebook()">Logout with Facebook</b-button>
        <b-button @click="getFacebookProfile()">getFacebookProfile</b-button>
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
    onSuccess(googleUser) {
      const profile = googleUser.getBasicProfile();
      console.log("profile: ", profile);
    },
    onFailure(error) {
      console.log(error);
    },
    signOut() {
      var auth2 = window.gapi.auth2.getAuthInstance();
      auth2.signOut().then(function() {
        console.log("User signed out.");
      });
    },
    // Facebook
    logInWithFacebook() {
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
    window.gapi.signin2.render("google-signin-button", {
      scope: "profile email",
      width: 240,
      height: 50,
      longtitle: true,
      onsuccess: this.onSuccess,
      onfailure: this.onFailure
    });
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
</style>
