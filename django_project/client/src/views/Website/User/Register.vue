<template>
  <b-container>
    <h1>Registraion</h1>

    <!-- Form 1 -->
    <div class="form-title">Account Information</div>
    <b-form @submit.prevent="handleSubmit">
      <!-- username -->
      <b-row class="mt-1">
        <b-col sm="3">
          <label class="form-label">
            User Name
            <em>*</em>
          </label>
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
            <span v-if="!$v.form.username.required">User name is required</span>
          </div>
        </b-col>
      </b-row>
      <!-- email -->
      <b-row class="mt-1">
        <b-col sm="3">
          <label class="form-label">
            Email
            <em>*</em>
          </label>
        </b-col>
        <b-col sm="9">
          <b-form-input
            size="sm"
            v-model="form.email"
            :class="{ 'is-invalid': submitted && $v.form.email.$error }"
          ></b-form-input>
          <div
            v-if="submitted && $v.form.email.$error"
            class="invalid-feedback"
          >
            <span v-if="!$v.form.email.required">Email is required</span>
            <span v-if="!$v.form.email.email">Email is invalid</span>
          </div>
        </b-col>
      </b-row>
      <!-- password -->
      <b-row class="mt-1">
        <b-col sm="3">
          <label class="form-label">
            Password
            <em>*</em>
          </label>
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
            <span v-if="!$v.form.password.required">Password is required</span>
            <span v-if="!$v.form.password.minLength"
              >Password must be at least 8 characters</span
            >
            <span v-if="!$v.form.password.lowercase">
              <br />Password must be at least 1 lowercase alphabetical character
            </span>
            <span v-if="!$v.form.password.upercase">
              <br />Password must be at least 1 uppercase alphabetical character
            </span>
            <span v-if="!$v.form.password.numeric">
              <br />Password must be at least 1 numeric character
            </span>
            <span v-if="!$v.form.password.character">
              <br />Password must be at least 1 special character
            </span>
          </div>
        </b-col>
      </b-row>
      <!-- confirm password -->
      <b-row class="mt-1">
        <b-col sm="3">
          <label class="form-label">
            Confirm Password
            <em>*</em>
          </label>
        </b-col>
        <b-col sm="9">
          <b-form-input
            size="sm"
            v-model="form.confirmPassword"
            type="password"
            aria-describedby="password-help-block"
            :class="{
              'is-invalid': submitted && $v.form.confirmPassword.$error
            }"
          ></b-form-input>
          <div
            v-if="submitted && $v.form.confirmPassword.$error"
            class="invalid-feedback"
          >
            <span v-if="!$v.form.confirmPassword.required"
              >Confirm Password is required</span
            >
            <span v-else-if="!$v.form.confirmPassword.sameAsPassword"
              >Passwords must match</span
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
          >Submit</b-button
        >
      </b-row>
    </b-form>
  </b-container>
</template>

<script>
import UserAPI from "@/api/site/user";

import {
  required,
  email,
  minLength,
  sameAs,
  helpers
} from "vuelidate/lib/validators";
// let strongRegex_for_backend_verify = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})");
let lowercase = helpers.regex("lowercase", /(?=.*[a-z])/);
let upercase = helpers.regex("upercase", /(?=.*[A-Z])/);
let numeric = helpers.regex("numeric", /(?=.*[0-9])/);
let character = helpers.regex("character", /(?=.*[!@#$%^&*])/);

export default {
  data() {
    return {
      form: {
        username: "",
        email: "",
        password: "",
        confirmPassword: ""
      },
      pre_files: [],
      submitted: false
    };
  },
  validations: {
    form: {
      username: {
        required
      },
      email: {
        required,
        email
      },
      password: {
        required,
        minLength: minLength(8),
        lowercase,
        upercase,
        numeric,
        character
      },
      confirmPassword: {
        required,
        sameAsPassword: sameAs("password")
      }
    }
  },
  methods: {
    async register() {
      let username = this.form.username;
      let email = this.form.email;
      let password = this.form.password;
      const payload = {
        username: username,
        email: email,
        password: password
      };
      const res = await UserAPI.register(payload);
      if (res.data) {
        console.log("register success", res.data);
        // this.$store.dispatch("user/login", {
        //   email,
        //   password
        // });
      } else {
        console.log("Fail", res.err);
      }
    },
    files_array_combine() {
      return this.pre_files.concat(this.form.files);
    },
    file_change() {
      // Step 1: Save the files to pre_files
      this.pre_files = this.files_array_combine();
    },
    file_remove_tag(tag) {
      // remove the tag in "files_total"
      const items = this.files_total;
      let filteredItems = items.filter(item => item !== tag);
      this.files_total = filteredItems;
    },
    handleSubmit() {
      this.submitted = true;

      // stop here if form is invalid
      this.$v.$touch();
      if (this.$v.$invalid) {
        return;
      }

      alert("SUCCESS!! :-)\n\n" + JSON.stringify(this.user));
    }
  },
  computed: {
    files_total: {
      get: function() {
        return this.files_array_combine();
      },
      set: function(value) {
        this.form.files = value;
        this.pre_files = [];
      }
    },
    BreadcrumbObject() {
      return {
        page: "Registraion",
        items: [
          {
            text: "Home",
            to: { path: "/" }
          },
          {
            text: "Login",
            to: { path: "/login" }
          },
          {
            text: "Registraion"
          }
        ]
      };
    }
  }
};
</script>

<style scoped>
#file-upload-btn {
  cursor: pointer;
  border-radius: 0;
}
#file-upload {
  opacity: 0;
  position: absolute;
  z-index: -1;
}
.button-item {
  background-color: #036ab5;
}
.form-title {
  border-spacing: 3px;
  font-size: 0.9em;
  background: #016ab3;
  color: #fff;
  font-weight: bold;
  height: 23px;
  padding-left: 10px;
}
.form-label {
  border-collapse: separate;
  border-spacing: 3px;
  font: inherit;
  vertical-align: top;
  font-size: 0.9em;
  margin: 0px;
  color: #047dbc;
  padding: 4px 3px;
  font-weight: bold;
}
</style>
