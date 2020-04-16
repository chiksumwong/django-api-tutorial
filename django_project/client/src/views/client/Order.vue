<template>
  <b-container>
    <h1>Products</h1>
    <li v-for="(item, index) in products" :key="index">
      <p>{{item.product_id}}</p>
      <p>{{item.product_name}}</p>
    </li>
  </b-container>
</template>

<script>
import ShopAPI from "@/api/shop";
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
      const res = await ShopAPI.listProducts();
      if (res.data) {
        this.products = res.data;
      } else {
        console.log("Fail", res.err);
      }
    }
  }
};
</script>

<style></style>
