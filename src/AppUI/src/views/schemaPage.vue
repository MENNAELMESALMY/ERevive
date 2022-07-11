<template>
  <div class="schemaPage">
    <div class="subTitle">Generated Schema !</div>
    <img src="../../public/assets/generatedSchema.png" alt="generatedSchema" />
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/Colors.scss";
.schemaPage {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  .subTitle {
    padding: 20px;
    font-size: 45px;
    font-weight: 700;
    font-family: "Indie Flower", cursive;
    text-align: center;
    color: $darkBlue;
  }
  img {
    width: 70%;
  }
}
@media screen and (max-width: 768px) {
  .schemaPage {
    .subTitle {
      font-size: 30px;
    }
  }
}
</style>

<script>
export default {
  name: "schemaPage",
};
</script>
