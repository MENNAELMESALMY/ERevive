<template>
  <div class="relationsDashboard">
    <div class="subTitle">Detected Cardinalities</div>
    <div class="content">
      <div class="box">
        <div class="circularBar" :data-goal="oneToOneCounter">
          <div class="percentValue" :data-goal="oneToOneCounter">0%</div>
        </div>
        <div class="subTitle">1:1</div>
      </div>
      <div class="box">
        <div class="circularBar" :data-goal="oneToMCounter">
          <div class="percentValue" :data-goal="oneToMCounter">0%</div>
        </div>
        <div class="subTitle">1:M</div>
      </div>
      <div class="box">
        <div class="circularBar" :data-goal="mToNCounter">
          <div class="percentValue" :data-goal="mToNCounter">0%</div>
        </div>
        <div class="subTitle">M:N</div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/Colors.scss";
.relationsDashboard {
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  border-radius: 12px;
  margin-top: 45px;
  padding: 20px;
}
.subTitle {
  padding: 20px;
  font-size: 30px;
  font-weight: 700;
  text-align: center;
  color: $darkBlue;
}
.content {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 20px;
  justify-items: center;
}
.circularBar {
  position: relative;
  height: 250px;
  width: 250px;
  background: linear-gradient(to right, $darkBlue, $lightBlue);
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.circularBar:before {
  content: "";
  position: absolute;
  height: 84%;
  width: 84%;
  background-color: white;
  border-radius: 50%;
}
.percentValue {
  position: relative;
  font-size: 50px;
  font-weight: 700;
  color: $darkBlue;
}
@media screen and (max-width: 1450px) {
  .content {
    grid-template-columns: 1fr;
  }
}
@media screen and (max-width: 990px) {
  .circularBar {
    width: 180px;
    height: 180px;
  }
}
@media screen and (max-width: 500px) {
  .relationsDashboard {
    padding: 5px;
  }
}
</style>

<script>
export default {
  name: "relationsDashboard",
  props: {
    oneToOneCounter: {
      type: Number,
      required: true,
    },
    oneToMCounter: {
      type: Number,
      required: true,
    },
    mToNCounter: {
      type: Number,
      required: true,
    },
  },
  created() {
    window.addEventListener("scroll", this.handleScroll);
  },
  destroyed() {
    window.removeEventListener("scroll", this.handleScroll);
  },
  //   mounted() {

  //   },
  methods: {
    handleScroll() {
      let circularBars = document.querySelectorAll(".circularBar");
      let percentValues = document.querySelectorAll(".percentValue");
      let box = document.querySelectorAll(".box");
      let goalScroll =
        window.scrollY + box[0].getBoundingClientRect().top - 600;
      if (window.scrollY >= goalScroll) {
        circularBars.forEach((circularBar) => this.startCount(circularBar));
        percentValues.forEach((percentValue) =>
          this.startCountPercent(percentValue)
        );
      }
    },
    startCount(circularBar) {
      let percent = 0;
      let goal = circularBar.getAttribute("data-goal");
      if (goal > 0) {
        let timer = setInterval(() => {
          percent += 1;
          circularBar.style.background = `conic-gradient(#1D1E4E ${
            percent * 3.6
          }deg, #D3D3D3 ${percent * 3.6}deg)`;
          if (percent == goal) {
            clearInterval(timer);
          }
        }, 20);
      }
      window.removeEventListener("scroll", this.handleScroll);
    },
    startCountPercent(percentValue) {
      let percent = 0;
      let goal = percentValue.getAttribute("data-goal");
      if (goal > 0) {
        let timer = setInterval(() => {
          percent += 1;
          percentValue.innerHTML = percent + "%";
          if (percent == goal) {
            clearInterval(timer);
          }
        }, 20);
      }
    },
  },
};
</script>
