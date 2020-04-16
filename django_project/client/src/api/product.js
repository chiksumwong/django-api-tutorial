import Vue from "vue";

const ProductAPI = {
  //List
  listProducts: () => Vue.prototype.$axios.get("/app/shop/product/"),
  createProduct: payload =>
    Vue.prototype.$axios.post("/app/shop/product/", payload),
  //Detail
  retrieveProduct: productId =>
    Vue.prototype.$axios.get("/app/shop/product/" + productId + "/"),
  updateProduct: (productId, payload) =>
    Vue.prototype.$axios.put("/app/shop/product/" + productId + "/", payload),
  deleteProduct: productId =>
    Vue.prototype.$axios.delete("/app/shop/product/" + productId + "/")
};

export default ProductAPI;
