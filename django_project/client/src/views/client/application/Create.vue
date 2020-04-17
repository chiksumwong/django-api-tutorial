<template>
  <b-container>
    <h1>Create Application</h1>
    <!-- Form 1 -->
    <b-form>
      <!-- Form 2 -->
      <div class="form-title mt-1">Customer Information</div>
      <!-- Company Name Eng-->
      <b-row class="mt-1">
        <b-col sm="3">
          <label class="form-label">
            Cusomter Name
            <em>*</em>
          </label>
        </b-col>
        <b-col sm="9">
          <b-form-input size="sm" v-model="form.customer_name"></b-form-input>
        </b-col>
      </b-row>

      <!-- button -->
      <b-row class="justify-content-end">
        <b-button
          squared
          variant="primary"
          size="sm"
          class="my-2 mx-3 button-item"
          @click="submit()"
          >Submit</b-button
        >
      </b-row>
    </b-form>
  </b-container>
</template>

<script>
import ApplicationAPI from "@/api/application";
export default {
  data() {
    return {
      form: {
        customer_name: ""
      }
    };
  },
  methods: {
    submit() {
      this.apply();
    },
    async apply() {
      const payload = {
        customer_name: this.form.customer_name
      };
      const res = await ApplicationAPI.createApplication(payload);
      if (res.data) {
        console.log("create application success", res.data);
        this.$router.push("/applications");
      } else {
        console.log("Fail", res.err);
      }
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
