<template>
  <b-container>
      <h1>
          List all Files
      </h1>
      <li v-for="(item, index) in files" :key="index">
      <p>{{item.id}}</p>
      <p>{{item.title}}</p>
      <p>{{item.file}}</p>
      <a :href="item.file">Link</a>
    </li>
  </b-container>
</template>

<script>
import FileAPI from "@/api/file";

export default {
  data() {
    return {
      files: []
    };
  },
  mounted() {
    this.loadFiles();
  },
  methods: {
    async loadFiles() {
      const res = await FileAPI.listFiles();
      if (res.data) {
        this.files = res.data;
      } else {
        console.log("Fail", res.err);
      }
    }
  }
};
</script>
