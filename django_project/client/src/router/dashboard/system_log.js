// import SystemLogCreate from "@/views/client/system_log/Create";
// import SystemLogUpdate from "@/views/client/system_log/Update";
// import SystemLog from "@/views/client/system_log/SystemLog";
import SystemLogs from "@/views/dashboard/system_log/SystemLogs";

export default [
  {
    path: "system_logs",
    name: "system_logs",
    component: SystemLogs
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
