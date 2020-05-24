<template>
  <div class="mx-3">
    <!-- Title -->
    <div class="row p-3">
      <div class="page">Access Log</div>
    </div>
    <div>
      <b-button
        variant="success"
        squared
        class="px-5 mb-2"
        @click="exportExcel()"
        >Export</b-button
      >
      <!-- Table -->
      <b-table
        class="table"
        :items="items"
        :fields="fields"
        :busy="isBusy"
        small
      >
        <!-- Busy loading -->
        <template v-slot:table-busy>
          <div class="text-center text-success my-2">
            <b-spinner class="align-middle"></b-spinner>
            <strong>Loading...</strong>
          </div>
        </template>
        <!-- End busy loading -->
        <!-- Select Checkbox Head -->
        <template v-slot:head(select)>
          <b-form-checkbox v-model="checked" @change="checkAll()">
          </b-form-checkbox>
        </template>
        <!-- End Select Checkbox Head -->
        <!-- Select Checkbox -->
        <template v-slot:cell(select)="row">
          <b-form-checkbox-group v-model="check_list">
            <b-form-checkbox :value="row.item.id"> </b-form-checkbox>
          </b-form-checkbox-group>
        </template>
        <!-- End Select Checkbox -->
      </b-table>
      <!-- End Table -->
    </div>
    <hr class="mt-0" />
    {{ check_list }}
  </div>
</template>

<script>
import XLSX from "xlsx";
import Formatter from "@/helper/formatter";

export default {
  data() {
    return {
      fields: [
        { key: "select", label: "#" },
        { key: "id", label: "ID" },
        { key: "company_name_e", label: "Company Name" },
        {
          key: "created_at",
          label: "Creation Time",
          formatter: value => {
            return Formatter.dateTimeFormatter(value);
          }
        },
        { key: "d_workflow", label: "Status" }
      ],
      items: [
        {
          id: "R001",
          company_name_e: "ABC Company",
          created_at: "01/04/2020",
          d_workflow: "Processing"
        }
      ],
      isBusy: false,
      check_list: [],
      checked: false
    };
  },
  methods: {
    checkAll() {
      this.checked = !this.checked;
    },
    tableFormatter(items) {
      let data = [];
      let header = ["ID", "Company Name", "Creation Time", "Status"];
      data.push(header);
      items.forEach(element => {
        let data_item = [];
        data_item.push(element.id);
        data_item.push(element.company_name_e);
        data_item.push(Formatter.dateTimeFormatter(element.created_at));
        data_item.push(element.d_workflow);
        data.push(data_item);
      });
      return data;
    },
    exportExcel() {
      const ws = XLSX.utils.aoa_to_sheet(this.tableFormatter(this.items));
      const wb = XLSX.utils.book_new();
      XLSX.utils.book_append_sheet(wb, ws);
      XLSX.writeFile(wb, "Registations.xlsx");
    },
    toggleBusy() {
      this.isBusy = !this.isBusy;
    },
    loadAccessLog() {
      return false;
    }
  },
  mounted() {
    this.loadAccessLog();
  }
};
</script>

<style scoped>
.page {
  color: #0069ae;
  font-size: 2em;
}
</style>
