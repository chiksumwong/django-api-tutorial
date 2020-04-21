import Vue from "vue";
// import { store } from "@/store";
import VueRouter from "vue-router";
import ClientLayout from "@/views/app/ClientLayout";
import DashboardLayout from "@/views/app/DashboardLayout";
import ClientHome from "@/views/client/product/Products";
import DashboardHome from "@/views/dashboard/Home";
import Files from "@/views/client/Files";
import ProductRoutes from "./client/product";
import ApplicationRoutes from "./client/application";
import SystemLogRoutes from "./dashboard/system_log";

import Registration from "@/views/client/Registration";

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
        path: "register",
        name: "registration",
        component: Registration
      },
      {
        path: "files",
        name: "files",
        component: Files
      },
      ...ProductRoutes,
      ...ApplicationRoutes,
      ...SystemLogRoutes
    ]
  },
  {
    path: "/dashboard",
    component: DashboardLayout,
    children: [
      {
        path: "",
        name: "dashboard_home",
        component: DashboardHome
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
//   const loggedIn = this.$store.state.user.t;
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
