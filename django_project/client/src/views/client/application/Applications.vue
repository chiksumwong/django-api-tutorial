<template>
  <b-container>
    <h1>Applications</h1>
    <div v-for="(item, index) in applications" :key="index">
      <b-card :title="item.customer_name">
        <b-card-text>{{ item.application_id }}</b-card-text>
        <b-button @click="go(item.application_id)" variant="primary"
          >View</b-button
        >
      </b-card>
    </div>
  </b-container>
</template>

<script>
import ApplicationAPI from "@/api/application";
export default {
  data() {
    return {
      applications: []
    };
  },
  mounted() {
    this.loadApplications();
  },
  methods: {
    async loadApplications() {
      const res = await ApplicationAPI.listApplications();
      if (res.data) {
        this.applications = res.data;
      } else {
        console.log("Fail", res.err);
      }
    },
    go(id) {
      this.$router.push("application/" + id);
    }
  }
};
</script>

<style></style>
