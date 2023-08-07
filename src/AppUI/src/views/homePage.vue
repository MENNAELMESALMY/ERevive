<template>
  <div class="home">
    <nav-bar />
    <div>
      <about-e-revive />
    </div>
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
import navBar from "../components/welcomePage/navBar.vue";
import aboutERevive from "../components/welcomePage/aboutERevive.vue";
export default {
  name: "homePage",
  components: {
    navBar,
    aboutERevive,
  },
  mounted() {
    this.$store.commit("predictedQueries/setAppFinished", false);
  },
};
</script>
