<template>
  <b-container>
    <h1>
      List all Files
    </h1>
    <div v-for="(item, index) in files" :key="index">
      <b-card :title="item.title">
        <b-card-text>{{ item.file }}</b-card-text>
        <b-card-text>{{ item.created_at }}</b-card-text>
        <a :href="item.file">Link</a>
      </b-card>
    </div>
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
