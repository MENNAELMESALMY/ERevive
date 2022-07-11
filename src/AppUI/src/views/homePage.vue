<template>
  <div class="home">
    <nav-bar />
    <div>
      <about-e-revive />
    </div>
    <div class="subTitle">What We Offer ?</div>
    <show-steps />
    <router-view />
    <footer-section />
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/Colors.scss";
.subTitle {
  background-color: $darkBlue;
  width: 100%;
  text-align: center;
  margin-top: 50px;
  margin-bottom: 50px;
  padding: 15px;
  padding-top: 30px;
  padding-bottom: 30px;
  font-size: 45px;
  font-family: "Indie Flower", cursive;
  font-weight: 700;
  color: white;
}
.ourTeam {
  text-align: center;
  margin-top: 70px;
  img {
    width: 25%;
  }
}
</style>

<script>
import showSteps from "../components/welcomePage/showSteps.vue";
import navBar from "../components/welcomePage/navBar.vue";
import aboutERevive from "../components/welcomePage/aboutERevive.vue";
import footerSection from "../components/welcomePage/footerSection.vue";
export default {
  name: "homePage",
  components: {
    showSteps,
    navBar,
    aboutERevive,
    footerSection,
  },
  mounted() {
    this.$store.commit("predictedQueries/setAppFinished", false);
  },
};
</script>
