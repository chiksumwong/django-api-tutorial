import Vue from "vue";

const ApplicationAPI = {
  //List
  listApplications: () => Vue.prototype.$axios.get("/a/shop/application/"),
  createApplication: payload =>
    Vue.prototype.$axios.post("/a/shop/application/", payload),
  //Detail
  retrieveApplication: applicationId =>
    Vue.prototype.$axios.get("/a/shop/application/" + applicationId + "/"),
  updateApplication: (applicationId, payload) =>
    Vue.prototype.$axios.put(
      "/a/shop/application/" + applicationId + "/",
      payload
    ),
  deleteApplication: applicationId =>
    Vue.prototype.$axios.delete("/a/shop/application/" + applicationId + "/")
};

export default ApplicationAPI;
