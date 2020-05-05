<template>
  <b-container>
    <h1>Products</h1>
    <li v-for="(item, index) in products" :key="index">
      <p>{{ item.product_id }}</p>
      <p>{{ item.product_name }}</p>
    </li>
  </b-container>
</template>

<script>
export default {
  data() {
    return {
      products: []
    };
  },
  mounted() {
    this.loadFiles();
  },
  methods: {}
};
</script>

<style></style>
