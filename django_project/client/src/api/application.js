import Vue from "vue";

const ApplicationAPI = {
  //List
  listApplications: () => Vue.prototype.$axios.get("/app/shop/application/"),
  createApplication: payload =>
    Vue.prototype.$axios.post("/app/shop/application/", payload),
  //Detail
  retrieveApplication: applicationId =>
    Vue.prototype.$axios.get("/app/shop/application/" + applicationId + "/"),
  updateApplication: (applicationId, payload) =>
    Vue.prototype.$axios.put(
      "/app/shop/application/" + applicationId + "/",
      payload
    ),
  deleteApplication: applicationId =>
    Vue.prototype.$axios.delete("/app/shop/application/" + applicationId + "/")
};

export default ApplicationAPI;
