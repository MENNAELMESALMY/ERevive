<template>
  <div class="card">
    <div class="tag" :style="{ 'background-color': colorHex }"></div>
    <h3>{{ title }}</h3>
    <p>{{ text }}</p>
    <button :style="{ 'background-color': colorHex }" >
      {{ buttonText }}
    </button>
  </div>
</template>

<style lang="scss" scoped>
.card {
  width: 400px;
  margin: 20px;
  padding: 30px;
  -webkit-box-shadow: 0px 0px 3px 3px #b9b7bd;
  -moz-box-shadow: 0px 0px 3px 3px #b9b7bd;
  box-shadow: 0px 0px 3px 3px #b9b7bd;
  position: relative;
}
.tag {
  position: absolute;
  top: 10px;
  right: 0px;
  width: 20%;
  height: 30px;
}
p {
  padding-bottom: 60px;
}
button {
  width: 60%;
  height: 60px;
  border: none;
  color: #fff;
  font-size: 16px;
  cursor: pointer;
  border-style: double;
  border-color: #fff;
  border-width: 10px;
  position: absolute;
  right: 20%;
  bottom: 20px;
}
button:hover {
  transform: scale(1.02);
}
button:active {
  transform: scale(1.02);
}
</style>

<script>
export default {
  name: "CardWithTag",
  props: {
    title: { type: String },
    text: { type: String },
    colorHex: { type: String },
    buttonText: { type: String },
  },
  computed: {},
  methods: {
    clickFuction() {
      return;
    },
  },
};
</script>
