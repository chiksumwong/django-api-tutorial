import Vue from "vue";
// import { store } from "@/store";
import VueRouter from "vue-router";
Vue.use(VueRouter);

// Layout
import WebsiteLayout from "@/views/App/WebsiteLayout";
import AdminPanelLayout from "@/views/App/AdminPanelLayout";
// Routes
import ProductRoutes from "./site/product";
import SystemLogRoutes from "./admin/system-log";
// Pages - Home
import WebsiteHome from "@/views/Website/Product/Products";
import AdminPanelHome from "@/views/AdminPanel/Dashboard/Dashboard";
// Pages - Website
import Register from "@/views/Website/User/Register";
import Login from "@/views/Website/User/Login";
// Pages - Admin Panel
import Dashboard from "@/views/AdminPanel/Dashboard/Dashboard";

const routes = [
  {
    path: "/",
    component: WebsiteLayout,
    children: [
      {
        path: "",
        name: "site_home",
        component: WebsiteHome
      },
      {
        path: "register",
        name: "register",
        component: Register
      },
      {
        path: "login",
        name: "login",
        component: Login
      },
      ...ProductRoutes
    ]
  },
  {
    path: "/admin",
    component: AdminPanelLayout,
    children: [
      {
        path: "",
        name: "admin_home",
        component: AdminPanelHome
      },
      {
        path: "dashboard",
        name: "dashboard",
        component: Dashboard
      },
      ...SystemLogRoutes
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
