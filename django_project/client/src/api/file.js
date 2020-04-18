import Vue from "vue";

const FileAPI = {
  listFiles: () => Vue.prototype.$axios.get("/f/file/")
};

export default FileAPI;
