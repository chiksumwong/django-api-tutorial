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
import Navbar from "@/components/AdminPanelLayout/Navbar";
import Footer from "@/components/AdminPanelLayout/Footer";
import Sidebar from "@/components/AdminPanelLayout/Sidebar";

export default {
  components: {
    Navbar,
    Footer,
    Sidebar
  }
};
</script>
