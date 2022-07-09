<template>
  <div class="stepsCard">
    <div class="right" v-if="direction == 'right'">
      <div class="textContent">
        <h3>{{ title }}</h3>
        <p>{{ description }}</p>
      </div>
      <div class="imageContent">
        <img :src="image" alt="Image" />
      </div>
    </div>
    <div class="left" v-if="direction == 'left'">
      <div class="textContent">
        <h3>{{ title }}</h3>
        <p>{{ description }}</p>
      </div>
      <div class="imageContent">
        <img :src="image" alt="Image" />
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "../../scss/Colors.scss";
.stepsCard {
  background-color: $veryLightBlue;
  color: $darkBlue;
  .left {
    display: flex;
    text-align: center;
    flex-direction: row-reverse;
  }
  .right {
    display: flex;
    flex-direction: row;
    text-align: center;
  }
  .textContent {
    width: 50%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-family: "Indie Flower", cursive;
    padding: 25px;
    h3 {
      font-weight: 700;
      font-size: 30px;
      padding-bottom: 10px;
    }
    p {
      font-size: 23px;
      padding: 10px;
      padding-right: 15px;
      padding-left: 15px;
    }
  }
  .imageContent {
    width: 50%;
    img {
      width: 100%;
      height: 100%;
    }
  }
}
@media screen and (max-width: 700px) {
  .left,
  .right {
    flex-wrap: wrap;
    .imageContent,
    .textContent {
      width: 100%;
    }
  }
}
</style>

<script>
export default {
  name: "stepsCard",
  props: {
    title: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
    image: {
      type: String,
      required: true,
    },
    direction: {
      type: String,
      required: true,
    },
  },
};
</script>
