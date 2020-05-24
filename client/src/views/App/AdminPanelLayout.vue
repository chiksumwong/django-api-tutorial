<template>
  <div>
    <div class="row mx-0">
      <div class="col-sm-2 px-0">
        <Sidebar />
      </div>
      <div class="col-sm-10 px-0">
        <div class="content">
          <Navbar />
          <router-view></router-view>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/AdminPanelLayout/Navbar";
import Sidebar from "@/components/AdminPanelLayout/Sidebar";

export default {
  components: {
    Navbar,
    Sidebar
  }
};
</script>
