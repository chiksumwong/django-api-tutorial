import ApplicationCreate from "@/views/client/application/Create";
// import ApplicationUpdate from "@/views/client/application/Update";
// import Application from "@/views/client/application/Application";
import Applications from "@/views/client/application/Applications";

export default [
  {
    path: "applications",
    name: "applications",
    component: Applications
  },
  {
    path: "application/create",
    name: "application_create",
    component: ApplicationCreate
  }
  // ,
  // {
  //   path: "application/:id",
  //   name: "application",
  //   component: Application
  // },
  // {
  //   path: "application/update/:id",
  //   name: "application_update",
  //   component: ApplicationUpdate
  // }
];
