<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<style>
html {
  position: relative;
  min-height: 100%;
}
.content {
  /* height of footer */
  margin-bottom: 80px;
}
.footer {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 60px;
}
</style>
