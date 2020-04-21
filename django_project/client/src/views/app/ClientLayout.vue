<template>
  <div>
    <Navbar />
    <div class="content">
      <router-view></router-view>
    </div>
    <Footer />
  </div>
</template>

<script>
import Navbar from "@/components/client_layout/Navbar";
import Footer from "@/components/client_layout/Footer";

export default {
  components: {
    Navbar,
    Footer
  }
};
</script>
