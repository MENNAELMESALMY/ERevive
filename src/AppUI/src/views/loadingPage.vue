<template>
  <div class="loadingPage">
    <div class="subTitle">Image Processing is Running ....</div>
    <div class="loader"></div>
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/Colors.scss";
.loadingPage {
  display: flex;
  flex-direction: column;
  //justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: white;
}
.subTitle {
  margin-top: 50px;
  padding: 20px;
  font-size: 45px;
  font-weight: 700;
  font-family: "Indie Flower", cursive;
  text-align: center;
  color: $darkBlue;
}
.loader {
  position: relative;
  margin-top: 50px;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background: linear-gradient(45deg, transparent, transparent 5%, $darkYellow);
  animation: animate 2s linear infinite;
}
@keyframes animate {
  0% {
    transform: rotate(0deg);
    filter: hue-rotate(0deg);
    //background-color: $darkBlue;
  }
  100% {
    transform: rotate(360deg);
    filter: hue-rotate(360deg);
    //background-color: $lightBlue;
  }
}
.loader:before {
  content: "";
  position: absolute;
  top: 6px;
  left: 6px;
  right: 6px;
  bottom: 6px;
  border-radius: 50%;
  z-index: 1000;
  background: white;
}
.loader:after {
  content: "";
  position: absolute;
  top: 0px;
  left: 0px;
  right: 0px;
  bottom: 0px;
  background: linear-gradient(45deg, transparent, transparent 40%, #e5f403);
  border-radius: 50%;
  z-index: 1000;
  z-index: 1;
  filter: blur(30px);
}
</style>

<script>
export default {
  name: "loadingPage",
};
</script>
