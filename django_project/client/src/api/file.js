import Vue from "vue";

const FileAPI = {
  listFiles: () => Vue.prototype.$axios.get("/files/")
};

export default FileAPI;
