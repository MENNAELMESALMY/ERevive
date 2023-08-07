<template>
  <div class="databaseSeeds">
    <div class="subTitle">Do You Want to Add Seeds To DataBase ?</div>
    <img src="../../public/assets/question-mark.png" alt="seedsImage" />
    <button class="customBtn" @click="addSeeds">Add Seeds</button>
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/Colors.scss";
@import "../scss/Button.scss";
.databaseSeeds {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  .subTitle {
    margin-top: 50px;
    padding: 20px;
    font-size: 45px;
    font-weight: 700;
    font-family: "Indie Flower", cursive;
    text-align: center;
    color: $darkBlue;
  }
  img {
    width: 450px;
    height: 450px;
  }
  .customBtn {
    margin-top: 40px;
    margin-bottom: 20px;
    width: 50%;
  }
}
@media screen and (max-width: 768px) {
  .databaseSeeds {
    img {
      width: 180px;
      height: 180px;
    }
    .customBtn {
      width: 80%;
    }
  }
}
</style>

<script>
export default {
  name: "databaseSeeds",
  methods: {
    addSeeds() {
      this.$store.dispatch("predictedQueries/postAddSeeds");
      this.$store.commit("triggerModals/toggleSavedModal");
    },
  },
};
</script>
