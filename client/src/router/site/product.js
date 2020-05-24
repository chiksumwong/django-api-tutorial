import ProductCreate from "@/views/Website/Product/Create";
import ProductUpdate from "@/views/Website/Product/Update";
import Product from "@/views/Website/Product/Product";
import Products from "@/views/Website/Product/Products";

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
