<template>
  <b-container>
    <h1>Applications</h1>
    <b-table
      ref="selectableTable"
      selectable
      select-mode="multi"
      :items="applications"
      :fields="fields"
      @row-selected="onRowSelected"
      responsive="sm"
    >
      <!-- Example scoped slot for select state illustrative purposes -->
      <template v-slot:cell(selected)="{ rowSelected }">
        <template v-if="rowSelected">
          <span aria-hidden="true">X</span>
          <span class="sr-only">Selected</span>
        </template>
        <template v-else>
          <span aria-hidden="true">&nbsp;</span>
          <span class="sr-only">Not selected</span>
        </template>
      </template>
    </b-table>
    <p>
      <b-button size="sm" @click="selectAllRows" class="mr-1"
        >Select all</b-button
      >
      <b-button size="sm" @click="clearSelected">Clear selected</b-button>
      <b-button size="sm" @click="update" class="ml-1" variant="success"
        >Update</b-button
      >
    </p>
    <p>
      Selected Rows:<br />
      {{ selected }}
    </p>
  </b-container>
</template>

<script>
import ApplicationAPI from "@/api/application";
export default {
  data() {
    return {
      fields: [
        "Select",
        {
          key: "application_id",
          label: "Application ID"
        },
        {
          key: "customer_name",
          label: "Customer Name"
        },
        {
          key: "status",
          label: "Status"
        },
        {
          key: "created_at",
          label: "Created At"
        }
      ],
      applications: [],
      selected: []
    };
  },
  mounted() {
    this.loadApplications();
  },
  methods: {
    onRowSelected(items) {
      this.selected = items;
    },
    selectAllRows() {
      this.$refs.selectableTable.selectAllRows();
    },
    clearSelected() {
      this.$refs.selectableTable.clearSelected();
    },
    async loadApplications() {
      const res = await ApplicationAPI.listApplications();
      if (res.data) {
        console.log("Load Application", res.data);
        this.applications = res.data;
      } else {
        console.log("Fail", res.err);
      }
    },
    go(id) {
      this.$router.push("application/" + id);
    },
    update() {
      return true;
    }
  }
};
</script>

<style></style>
