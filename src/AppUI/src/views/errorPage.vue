<template>
  <div class="errorPage">
    <img src="../../public/assets/close.png" alt="error_image" />
    <h2>Sorry, an error has occurred, please try again later.</h2>
    <p>
      <router-link to="/">
        <button class="customBtn">Return to Home</button>
      </router-link>
    </p>
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/Button.scss";
.errorPage {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  height: 100vh;
  h2 {
    font-size: 30px;
    font-weight: 700;
    margin: 30px;
    color: #c30010;
  }
  .customBtn {
    margin: 30px;
  }
}
</style>

<script>
export default {
  name: "errorPage",
};
</script>
