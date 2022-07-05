<template>
  <div class="footerSection">
    <p>© 2022 ERevive</p>
  </div>
</template>

<style lang="scss" scoped>
@import "../../scss/Colors.scss";
.footerSection {
  width: 100%;
  background-color: $darkBlue;
  padding-top: 25px;
  padding-bottom: 10px;
  text-align: center;
  letter-spacing: 0.1em;
  font-size: 22px;
  font-weight: 700;
  font-family: "Indie Flower", cursive;
  margin-top: 70px;
  color: white;
}
</style>

<script>
export default {
  name: "footerSection",
};
</script>
