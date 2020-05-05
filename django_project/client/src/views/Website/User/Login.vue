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
            variant="primary"
            size="sm"
            class="my-2 mx-3 button-item"
            type="submit"
            >Login</b-button
          >
        </b-row>
        <!-- <router-link to="/register"> Register </router-link><br />
        <router-link to="/forgot_password">Forgot Password</router-link> -->
        <div class="g-signin2" data-onsuccess="onSignIn"></div>
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
    onSignIn(googleUser) {
      var profile = googleUser.getBasicProfile();
      console.log("ID: " + profile.getId()); // Do not send to your backend! Use an ID token instead.
      console.log("Name: " + profile.getName());
      console.log("Image URL: " + profile.getImageUrl());
      console.log("Email: " + profile.getEmail()); // This is null if the 'email' scope is not present.
    },
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
