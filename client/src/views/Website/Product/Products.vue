<template>
  <b-container>
    <div class="row" v-for="(item, index) in products" :key="index">
      <div class="col-md-4">
        <b-card
          :title="item.product_name"
          img-src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTqS_jGypX_ODjS2xPUWQT0j45ZL3-QyNW8-oEx9092wfr3q6xVXFa28RlMTdeNZcHnaQku03o&usqp=CAc"
          style="max-width: 20rem;"
          class="my-2 shadow-sm"
          @click="go(item.product_id)"
        >
          <b-card-text>Price: $ {{ item.price }}</b-card-text>
          <b-card-text>{{ item.description }}</b-card-text>
          <div class="d-flex justify-content-between align-items-center">
            <div class="btn-group">
              <!-- <button
                type="button"
                class="btn btn-sm btn-outline-secondary"
                @click="go(item.product_id)"
              >
                View
              </button> -->
              <!-- <button type="button" class="btn btn-sm btn-outline-secondary">
                Edit
              </button> -->
            </div>
            <small class="text-muted">{{ item.created_at }}</small>
          </div>
        </b-card>
      </div>
    </div>
  </b-container>
</template>

<script>
import ProductAPI from "@/api/site/product";

export default {
  data() {
    return {
      products: [
        {
          product_id: "001",
          product_name: "Iphone",
          description: "this is good product",
          price: 10000,
          created_at: "1/4/2020"
        }
      ]
    };
  },
  mounted() {
    this.loadProducts();
  },
  methods: {
    async loadProducts() {
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
