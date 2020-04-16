import Vue from "vue";
// import { store } from "@/store";
import VueRouter from "vue-router";
import ClientLayout from "@/views/app/ClientLayout";

import ClientHome from "@/views/client/Home";

import ProductCreate from "@/views/client/product/Create";
import ProductUpdate from "@/views/client/product/Update";
import Product from "@/views/client/product/Product";
import Products from "@/views/client/product/Products";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    component: ClientLayout,
    children: [
      {
        path: "",
        name: "client_home",
        component: ClientHome
      },
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
    ]
  },
  {
    path: "*",
    redirect: "/"
  }
];

export const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

// router.beforeEach((to, from, next) => {
//   const publicPages = [
//     "client_home",
//   ];

//   const userPages = [
//     "tender_notice",
//     "tenders",
//     "tender",
//     "pos",
//     "po",
//     "vender"
//   ];

//   const adminPages = [
//     "dashboard",
//     "registration",
//     "database",
//     "po_management",
//     "tender_management",
//     "vendor_management",
//     "access_log",
//     "audit_log",
//     "sync_log"
//   ];

//   const authRequired = publicPages.includes(to.name);
//   const authAdminRequired = adminPages.includes(to.name);
//   const authUserRequired = userPages.includes(to.name);
//   const loggedIn = localStorage.getItem("token");
//   const isAdmin = store.state.user.isAdmin;

//   if (loggedIn) {
//     if (isAdmin) {
//       if (authRequired || authUserRequired) {
//         return next("/dashboard");
//       }
//     } else {
//       next();
//       if (authRequired || authAdminRequired) {
//         return next("/");
//       }
//     }
//   } else {
//     if (!authRequired) {
//       return next("/login");
//     }
//   }
//   next(); //for public page
// });
