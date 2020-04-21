<template>
  <b-container>
    <h1>System Logs</h1>
    <b-table small :fields="fields" :items="systemLogs" responsive="sm">
      <template v-slot:cell(index)="data">
        {{ data.index + 1 }}
      </template>
      <template v-slot:cell(log)="data">
        <b class="text-info">{{ data.item.log.toUpperCase() }}</b>
      </template>
    </b-table>
  </b-container>
</template>

<script>
import SystemLogAPI from "@/api/system_log";
export default {
  data() {
    return {
      fields: [
        "index",
        { key: "log", label: "Log" },
        { key: "message", label: "Message" },
        { key: "status", label: "Status" },
        { key: "system_log_id", label: "Log ID" },
        { key: "created_at", label: "Created At" }
      ],
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
        console.log("Load System Log", res.data);
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
