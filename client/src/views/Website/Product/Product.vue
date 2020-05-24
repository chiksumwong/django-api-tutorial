<template>
  <b-container>
    <h1>Product</h1>
    <div>
      <b-card :title="product.product_name">
        <b-card-text>Price: $ {{ product.price }}</b-card-text>
        <b-card-text>{{ product.created_at }}</b-card-text>
        <b-button @click="buy(product.product_id)" variant="primary"
          >Buy</b-button
        >
        <b-button
          @click="goEdit(product.product_id)"
          variant="success"
          class="ml-2"
          >Edit</b-button
        >
        <b-button
          @click="godelete(product.product_id)"
          variant="danger"
          class="ml-2"
          >Delte</b-button
        >
      </b-card>
    </div>
  </b-container>
</template>

<script>
import ProductAPI from "@/api/site/product";
export default {
  data() {
    return {
      product: []
    };
  },
  mounted() {
    this.loadProduct();
  },
  methods: {
    async loadProduct() {
      const res = await ProductAPI.retrieveProduct(this.$route.params.id);
      if (res.data) {
        console.log("load product success", res.data);
        this.product = res.data;
      } else {
        console.log("Fail", res.err);
      }
    },
    buy(id) {
      alert("Buy: " + id);
    },
    goEdit(id) {
      this.$router.push("update/" + id);
    },
    async godelete() {
      const res = await ProductAPI.deleteProduct(this.$route.params.id);
      console.log(res);
      if (res.data === "") {
        console.log("delete product success", res.data);
        this.$router.push("/products");
      } else {
        console.log("Fail", res.err);
      }
    }
  }
};
</script>

<style></style>
