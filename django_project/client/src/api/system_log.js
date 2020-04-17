import Vue from "vue";

const SystemLogAPI = {
  //List
  listSystemLogs: () => Vue.prototype.$axios.get("/function/system_log/log/"),
  createSystemLog: payload =>
    Vue.prototype.$axios.post("/function/system_log/log/", payload),
  //Detail
  retrieveSystemLog: system_logId =>
    Vue.prototype.$axios.get("/function/system_log/log/" + system_logId + "/"),
  updateSystemLog: (system_logId, payload) =>
    Vue.prototype.$axios.put(
      "/function/system_log/log/" + system_logId + "/",
      payload
    ),
  deleteSystemLog: system_logId =>
    Vue.prototype.$axios.delete(
      "/function/system_log/log/" + system_logId + "/"
    )
};

export default SystemLogAPI;
