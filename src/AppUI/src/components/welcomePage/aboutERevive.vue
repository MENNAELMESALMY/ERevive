<template>
  <div class="aboutERevive">
    <div class="aboutUs">
      ERevive is a Desktop Application that bridge the gap between developers
      understanding of customers' system requirements by providing a fast
      automated implementation for the first prototype of website and Save time
      by automating repetitive tasks done by software developers, by taking an
      ER diagram image as an input and outputs source code for SQL schema,
      queries, API and Website User interface for basic crud operation on
      entities as well as suggested top queries.
    </div>
    <div>
      <router-link to="/systemInfo">
        <button class="customBtn">
          LET'S START &nbsp;<i class="fa fa-arrow-right"></i>
        </button>
      </router-link>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "../../scss/Colors.scss";
@import "../../scss/Button.scss";
.aboutERevive {
  background-color: $darkGray;
  width: 100%;
  text-align: center;
  align-content: center;
  .aboutUs {
    padding: 50px;
    padding-bottom: 20px;
    letter-spacing: 0.1rem;
    line-height: 3.2;
    text-align: center;
    align-items: center;
    font-size: 25px;
    font-weight: 700;
    color: white;
    font-family: "Indie Flower", cursive;
  }
  .customBtn {
    margin-top: 25px;
    margin-bottom: 45px;
  }
}
</style>

<script>
export default {
  name: "aboutERevive",
};
</script>
