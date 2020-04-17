<template>
  <b-container>
    <h1>System Logs</h1>
    <div v-for="(item, index) in systemLogs" :key="index">
      <b-card :title="item.log">
        <b-card-text>{{ item.message }}</b-card-text>
        <b-card-text>{{ item.status }}</b-card-text>
        <b-button @click="go(item.system_log_id)" variant="primary"
          >View</b-button
        >
      </b-card>
    </div>
  </b-container>
</template>

<script>
import SystemLogAPI from "@/api/system_log";
export default {
  data() {
    return {
      systemLogs: []
    };
  },
  mounted() {
    this.loadSystemLogs();
  },
  methods: {
    async loadSystemLogs() {
      const res = await SystemLogAPI.listSystemLogs();
      if (res.data) {
        this.systemLogs = res.data;
      } else {
        console.log("Fail", res.err);
      }
    },
    go(id) {
      this.$router.push("system_log/" + id);
    }
  }
};
</script>

<style></style>
