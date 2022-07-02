
<template>
  <div class="cardDesign">
    <div class="card-style" :style="backgroundStyle"></div>
    <div class="card-header">
      <h5 class="card-title">{{ title }}</h5>
    </div>
    <div class="card-body">
      <p class="card-text">{{ description }}</p>
    </div>
    <div class="card-bottom" :style="backgroundStyle">
      <router-link :to="title"><button>CLICK ME!</button></router-link>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.cardDesign {
  max-width: 20em;
  margin-top: 20px;
  margin-bottom: 20px;
  background-color: white;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
  padding: 15px;
  text-align: center;
  overflow: hidden;
  position: relative;
  border-radius: 30px;
}
.card-style {
  &:before {
    position: absolute;
    margin: -6em;
    margin-left: -1em;
    padding: 7em;
    border-radius: 50%;
    box-shadow: 0 0 7px rgb(122, 122, 121);
    background-color: var(--bg-color);
    content: "";
  }
}
.card-header {
  padding-top: 35px;
  .card-title {
    font-size: 25px;
    font-weight: 700;
    position: relative;
    z-index: 9;
    color: black;
  }
}
.card-body {
  .card-text {
    font-size: 17px;
    color: black;
  }
}
.card-bottom {
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
    border-radius: 25px;
    box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease 0s;
  }
  button:hover {
    background-color: var(--bg-color);
    box-shadow: 0px 15px 20px rgba(122, 122, 121, 0.4);
    color: white;
    transform: translateY(-3px);
  }
}
</style>

<script>
import { mapState } from "vuex";
export default {
  name: "cardDesign",
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

        