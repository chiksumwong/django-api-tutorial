import Vue from "vue";

const ProductAPI = {
  //List
  listProducts: () => Vue.prototype.$axios.get("/a/shop/product/"),
  createProduct: payload =>
    Vue.prototype.$axios.post("/a/shop/product/", payload),
  //Detail
  retrieveProduct: productId =>
    Vue.prototype.$axios.get("/a/shop/product/" + productId + "/"),
  updateProduct: (productId, payload) =>
    Vue.prototype.$axios.put("/a/shop/product/" + productId + "/", payload),
  deleteProduct: productId =>
    Vue.prototype.$axios.delete("/a/shop/product/" + productId + "/")
};

export default ProductAPI;
