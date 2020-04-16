import Vue from "vue";

const FileAPI = {
  listFiles: () => Vue.prototype.$axios.get("/upload/file/")
};

export default FileAPI;
