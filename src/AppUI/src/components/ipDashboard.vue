<template>
  <div class="ipDashboard">
    <div class="counter">
      <div class="num" :data-goal="entitiesCounter">0</div>
      <div class="name">Number of Detected Entities</div>
    </div>
    <div class="counter">
      <div class="num" :data-goal="relationsCounter">0</div>
      <div class="name">Number of Detected Relations</div>
    </div>
    <div class="counter">
      <div class="num" :data-goal="attributesCounter">0</div>
      <div class="name">Number of Detected Attributes</div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/Colors.scss";
.ipDashboard {
  width: 100%;
  padding: 20px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 45px;
  justify-items: center;
  align-items: center;
  .counter {
    font-size: 50px;
    font-weight: 700;
    color: $darkBlue;
    text-align: center;
    width: 100%;
    height: 100%;
    padding: 30px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    border-radius: 12px;
    .name {
      font-weight: 500;
      font-size: 20px;
    }
  }
}
@media screen and (max-width: 700px) {
  .ipDashboard {
    grid-template-columns: repeat(1, 1fr);
    grid-gap: 20px;
    .counter {
      font-size: 30px;
      .num {
        font-size: 30px;
      }
      .name {
        font-size: 20px;
      }
    }
  }
}
</style>

<script>
export default {
  name: "ipDashboard",
  mounted() {
    let nums = document.querySelectorAll(".num");
    nums.forEach((num) => this.startCount(num));
  },
  methods: {
    startCount(element) {
      let goal = element.getAttribute("data-goal");
      if (goal > 0) {
        let count = setInterval(() => {
          element.textContent++;
          if (element.textContent == goal) {
            clearInterval(count);
          }
        }, 10);
      }
    },
  },
  props: {
    entitiesCounter: {
      type: Number,
      required: true,
    },
    relationsCounter: {
      type: Number,
      required: true,
    },
    attributesCounter: {
      type: Number,
      required: true,
    },
  },
};
</script>
