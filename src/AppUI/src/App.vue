<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  data() {
    return {};
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
