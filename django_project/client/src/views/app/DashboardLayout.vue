<template>
  <div>
    <Sidebar />
    <Navbar />
    <div class="content">
      <router-view></router-view>
    </div>
    <Footer />
  </div>
</template>

<script>
import Navbar from "@/components/dashboard_layout/Navbar";
import Footer from "@/components/dashboard_layout/Footer";
import Sidebar from "@/components/dashboard_layout/Sidebar";

export default {
  components: {
    Navbar,
    Footer,
    Sidebar
  }
};
</script>
