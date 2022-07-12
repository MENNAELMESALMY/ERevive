<template>
  <div class="lastPage">
    <div class="subTitle">All Done !</div>
    <img src="../../public/assets/thank-you.png" alt="thank-you" />
    <div class="subTitle" id="thanks">Thank you for using ERevive</div>
    <div class="subTitle">GoodBye till we meet again !</div>
    <div class="controlBtns">
      <router-link to="/">
        <button class="customBtn">Return To Home Page</button>
      </router-link>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/Colors.scss";
@import "../scss/Button.scss";
.lastPage {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 40px;
  img {
    width: 250px;
    height: 250px;
  }
  .subTitle {
    padding: 20px;
    font-size: 45px;
    font-weight: 700;
    font-family: "Indie Flower", cursive;
    text-align: center;
    color: $darkBlue;
  }
  #thanks {
    margin-top: 20px;
  }
}
.controlBtns {
  width: 100%;
  text-align: center;
  margin-top: 45px;
  .customBtn {
    width: 50%;
    margin: 12px;
  }
}
@media screen and (max-width: 768px) {
  .lastPage {
    img {
      width: 170px;
      height: 170px;
    }
  }
  .controlBtns {
    margin-top: 20px;
    .customBtn {
      width: 80%;
    }
  }
}
</style>

<script>
export default {
  name: "lastPage",
};
</script>
