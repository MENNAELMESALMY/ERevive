<template>
  <div class="cardDesign3" :style="backgroundStyle">
    <div class="cardDesign3-header">
      <h5 class="card-title">{{ title }}</h5>
    </div>
    <div class="cardDesign3-body">
      <p class="card-text">{{ description }}</p>
    </div>
    <div class="cardDesign3-footer">
      <button>CLICK ME!</button>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.cardDesign3 {
  max-width: 20em;
  margin-top: 20px;
  margin-bottom: 20px;
  background-image: linear-gradient(to bottom right, var(--bg-color), black);
  text-align: center;
  color: white;
  border-radius: 25px;
}
.cardDesign3-header {
  padding-top: 30px;
  .card-title {
    margin-bottom: 10px;
    font-size: 25px;
    font-weight: 700;
  }
}
.cardDesign3-body {
  padding: 15px;
  .card-text {
    font-size: 17px;
    margin-bottom: 20px;
  }
}
.cardDesign3-footer {
  padding: 15px;
  padding-top: 25px;
  padding-bottom: 25px;
  button {
    width: 70%;
    height: 50px;
    padding: 15px;
    font-size: 17px;
    font-weight: 700;
    border: none;
    cursor: pointer;
    color: white;
    letter-spacing: 1.8px;
    background-color: transparent;
    border: 2px solid var(--bg-color);
    box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease 0s;
  }
  button:hover {
    background-color: var(--bg-color);
    box-shadow: 0px 3px 8px rgba(122, 122, 121, 0.4);
    transform: translateY(-3px);
  }
}
</style>

<script>
import { mapState } from "vuex";
export default {
  name: "cardDesign3",
  props: {
    title: {
      type: String,
    },
    description: {
      type: String,
    },
  },
  computed: {
    ...mapState({
      themeColor: (state) => state.colorPallete.themeColor,
    }),
    backgroundStyle() {
      return {
        "--bg-color": this.themeColor,
      };
    },
  },
};
</script>
