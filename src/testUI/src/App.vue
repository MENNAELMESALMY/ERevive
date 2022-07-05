<template>
  <div id="app">
    <homePage />
  </div>
</template>

<script>
import homePage from "./views/homePage.vue";
export default {
  data() {
    return {};
  },
  components: {
    homePage,
  },
};
</script>

<style lang="scss">
@import "./scss/Colors.scss";
#app {
  margin: 0;
  padding: 0;
}
*,
body {
  padding: 0;
  margin: 0;
}
</style>
