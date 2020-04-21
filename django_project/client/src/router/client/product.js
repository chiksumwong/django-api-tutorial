import ProductCreate from "@/views/client/product/Create";
import ProductUpdate from "@/views/client/product/Update";
import Product from "@/views/client/product/Product";
import Products from "@/views/client/product/Products";

export default [
  {
    path: "products",
    name: "products",
    component: Products
  },
  {
    path: "product/create",
    name: "product_create",
    component: ProductCreate
  },
  {
    path: "product/:id",
    name: "product",
    component: Product
  },
  {
    path: "product/update/:id",
    name: "product_update",
    component: ProductUpdate
  }
];
