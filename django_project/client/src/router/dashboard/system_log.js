// import SystemLogCreate from "@/views/client/system_log/Create";
// import SystemLogUpdate from "@/views/client/system_log/Update";
// import SystemLog from "@/views/client/system_log/SystemLog";
import AccessLog from "@/views/dashboard/system_log/AccessLog";

export default [
  {
    path: "access_log",
    name: "access_log",
    component: AccessLog
  }
  //   ,
  //   {
  //     path: "system_log/create",
  //     name: "system_log_create",
  //     component: SystemLogCreate
  //   },
  //   {
  //     path: "system_log/:id",
  //     name: "system_log",
  //     component: SystemLog
  //   },
  //   {
  //     path: "system_log/update/:id",
  //     name: "system_log_update",
  //     component: SystemLogUpdate
  //   }
];
