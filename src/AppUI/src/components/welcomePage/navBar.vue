<template>
  <div class="navBar">
    <div class="logo">ERevive</div>
  </div>
</template>

<style lang="scss" scoped>
@import "../../scss/Colors.scss";
.navBar {
  width: 100%;
  background-color: $darkBlue;
  .logo {
    font-family: "Indie Flower", cursive;
    color: $darkGray;
    font-size: 40px;
    font-weight: 700;
    padding: 15px;
    color: white;
  }
}
</style>

<script>
export default {
  name: "navBar",
};
</script>
