<template>
  <div class="card">
    <div class="header" :style="{ 'background-color': colorHex }">
      <h3>{{ title }}</h3>
    </div>
    <h3>{{ subData[idx].subtitle }}</h3>
    <p>{{ subData[idx].text }}</p>
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
  data: function () {
    return {
      idx: 0,
    };
  },
  props: {
    title: { type: String },
    subData: { type: Array },
    colorHex: { type: String },
  },
  computed: {},
  methods: {
    clickFuction() {
      return;
    },
  },
};
</script>
