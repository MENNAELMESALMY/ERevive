<template>
  <div class="datatypeDashboard">
    <div class="datatype">
      <h3>String</h3>
      <div class="datatypesNum">
        <span
          class="slider"
          style="width: 0"
          :data-width="stringTypePercent + '%'"
        ></span>
      </div>
      <h6>{{ stringTypePercent }}%</h6>
    </div>
    <div class="datatype">
      <h3>Integer</h3>
      <div class="datatypesNum">
        <span
          class="slider"
          style="width: 0"
          :data-width="intTypePercent + '%'"
        ></span>
      </div>
      <h6>{{ intTypePercent }}%</h6>
    </div>
    <div class="datatype">
      <h3>Float</h3>
      <div class="datatypesNum">
        <span
          class="slider"
          style="width: 0"
          :data-width="floatTypePercent + '%'"
        ></span>
      </div>
      <h6>{{ floatTypePercent }}%</h6>
    </div>
    <div class="datatype">
      <h3>Boolean</h3>
      <div class="datatypesNum">
        <span
          class="slider"
          style="width: 0"
          :data-width="boolTypePercent + '%'"
        ></span>
      </div>
      <h6>{{ boolTypePercent }}%</h6>
    </div>
    <div class="datatype">
      <h3>Datetime</h3>
      <div class="datatypesNum">
        <span
          class="slider"
          style="width: 0"
          :data-width="dateTypePercent + '%'"
        ></span>
      </div>
      <h6>{{ dateTypePercent }}%</h6>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/Colors.scss";
.datatypeDashboard {
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  border-radius: 12px;
  color: $darkBlue;
  padding: 20px;
  .datatype {
    display: grid;
    grid-template-columns: 120px auto 30px;
    grid-gap: 20px;
    padding: 15px;
    .datatypesNum {
      width: 100%;
      height: 20px;
      position: relative;
      margin-top: 10px;
      background-color: white;
      border-radius: 0 7px 7px 0;
      span {
        position: absolute;
        left: 0;
        top: 0;
        height: 100%;
        border-radius: 0 7px 7px 0;
        background: linear-gradient(to right, $darkBlue, $lightBlue);
        transition: width 2s linear;
      }
    }
    h6 {
      padding-top: 12px;
    }
  }
}
@media screen and (max-width: 990px) {
  .datatypeDashboard {
    .datatype {
      padding-top: 10px;
      grid-template-columns: 1fr;
      grid-gap: 10px;
    }
  }
}
</style>

<script>
export default {
  name: "datatypesDashboard",
  props: {
    stringTypePercent: {
      type: Number,
      required: true,
    },
    intTypePercent: {
      type: Number,
      required: true,
    },
    floatTypePercent: {
      type: Number,
      required: true,
    },
    boolTypePercent: {
      type: Number,
      required: true,
    },
    dateTypePercent: {
      type: Number,
      required: true,
    },
  },
  mounted() {
    let spans = document.querySelectorAll(".slider");
    spans.forEach((span) => {
      let interval = setInterval(() => {
        span.style.width = span.getAttribute("data-width");
        clearInterval(interval);
      }, 10);
    });
  },
};
</script>
