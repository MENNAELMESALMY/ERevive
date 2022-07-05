<template>
  <div class="stepsCard">
    <h3>{{ title }}</h3>
    <p>{{ description }}</p>
  </div>
</template>

<style lang="scss" scoped>
@import "../../scss/Colors.scss";
.stepsCard {
  text-align: center;
  margin-top: 50px;
  width: 100%;
  height: 250px;
  background-color: $darkGray;
  border-radius: 12px;
  box-shadow: 0 3px 3px $lightYellow;
  color: white;
  padding: 30px;
  padding-top: 30px;
  transition: all 0.3s ease 0s;
  &:hover {
    box-shadow: 0 6px 6px $lightYellow;
    transform: translateY(-5px);
  }
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
  },
};
</script>
