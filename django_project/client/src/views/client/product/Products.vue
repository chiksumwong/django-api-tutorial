<template>
  <b-container>
    <h1>Products</h1>
    <div v-for="(item, index) in products" :key="index">
      <b-card :title="item.product_name">
        <b-card-text>Price: $ {{ item.price }}</b-card-text>
        <b-card-text>{{ item.created_at }}</b-card-text>
        <b-button @click="go(item.product_id)" variant="primary">View</b-button>
      </b-card>
    </div>
  </b-container>
</template>

<script>
import ProductAPI from "@/api/product";
export default {
  data() {
    return {
      products: []
    };
  },
  mounted() {
    this.loadFiles();
  },
  methods: {
    async loadFiles() {
      const res = await ProductAPI.listProducts();
      if (res.data) {
        this.products = res.data;
      } else {
        console.log("Fail", res.err);
      }
    },
    go(id) {
      this.$router.push("product/" + id);
    }
  }
};
</script>

<style></style>
