<template>
  <b-container>
    <h1>Create Product</h1>
    <div>
      <b-form>
        <b-form-group label="Product name:">
          <b-form-input
            v-model="form.product_name"
            type="text"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group label="Price">
          <b-form-input v-model="form.price" required></b-form-input>
        </b-form-group>

        <b-button @click="submit()" variant="primary">Submit</b-button>
        <b-button @click="reset()" variant="danger" class="ml-1"
          >Reset</b-button
        >
      </b-form>
    </div>
  </b-container>
</template>

<script>
import ProductAPI from "@/api/site/product";
export default {
  data() {
    return {
      form: {
        product_name: "",
        price: null
      }
    };
  },
  methods: {
    submit() {
      this.createProduct();
    },
    reset() {
      // Reset our form values
      this.form.product_name = "";
      this.form.price = "";
    },
    async createProduct() {
      const payload = {
        product_name: this.form.product_name,
        price: this.form.price
      };
      const res = await ProductAPI.createProduct(payload);
      if (res.data) {
        console.log("create product success", res.data);
        this.$router.push("/products");
      } else {
        console.log("Fail", res.err);
        this.$router.push("/");
      }
    }
  }
};
</script>
