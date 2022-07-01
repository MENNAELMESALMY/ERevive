
<template>
  <div class="cardDesign2" :style="backgroundStyle">
    <div class="card-style"></div>
    <div class="cardDesign2-header">
      <h5 class="card-title">{{ title }}</h5>
    </div>
    <div class="cardDesign2-body">
      <p class="card-text">{{ description }}</p>
    </div>
    <div class="cardDesign2-footer">
      <button>CLICK ME!</button>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.cardDesign2 {
  max-width: 20em;
  margin-top: 20px;
  margin-bottom: 20px;
  background-color: white;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
  text-align: center;
  border-radius: 25px;
}
.card-style {
  padding-top: 17px;
  //background-color: var(--bg-color);
  background-image: linear-gradient(to bottom right, var(--bg-color), black);
  border-top-left-radius: 25px;
  border-top-right-radius: 25px;
}
.cardDesign2-header {
  padding-top: 30px;
  .card-title {
    margin-bottom: 10px;
    font-size: 25px;
    font-weight: 700;
  }
}
.cardDesign2-body {
  padding: 15px;
  .card-text {
    font-size: 17px;
    margin-bottom: 20px;
  }
}
.cardDesign2-footer {
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
    color: var(--bg-color);
    letter-spacing: 1.8px;
    background-color: transparent;
    border: 2px solid var(--bg-color);
    box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease 0s;
  }
  button:hover {
    //background-color: var(--bg-color);
    background-image: linear-gradient(to bottom right, var(--bg-color), black);
    border: none;
    box-shadow: 0px 15px 20px rgba(122, 122, 121, 0.4);
    color: white;
    transform: translateY(-3px);
  }
}
</style>

<script>
import { mapState } from "vuex";
export default {
  name: "cardDesign2",
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
      themeColor: (state) => state.color_pallete.themeColor,
    }),
    backgroundStyle() {
      return {
        "--bg-color": this.themeColor,
      };
    },
  },
};
</script>

    