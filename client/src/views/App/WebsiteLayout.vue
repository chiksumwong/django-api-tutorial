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
import Navbar from "@/components/WebsiteLayout/Navbar";
import Footer from "@/components/WebsiteLayout/Footer";

export default {
  components: {
    Navbar,
    Footer
  }
};
</script>
