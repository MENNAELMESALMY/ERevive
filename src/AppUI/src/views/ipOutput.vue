<template>
  <div class="ipOutput">
    <div class="content">
      <div class="subTitle">What we get from Image Processing !</div>
      <ip-dashboard
        :entitiesCounter="100"
        :relationsCounter="250"
        :attributesCounter="50"
      />
      <div class="showStatistics">
        <div class="firstSection">
          <datatypes-dashboard
            :stringTypePercent="90"
            :intTypePercent="10"
            :floatTypePercent="45"
            :boolTypePercent="30"
            :dateTypePercent="58"
          />
        </div>
        <div class="secondSection">
          <show-info-table
            :primaryKeysCount="12"
            :multivaluedCount="5"
            :identifyingCount="7"
            :weakEntitiesCount="3"
            :naryCount="2"
            :fullCount="4"
            :partialCount="7"
          />
        </div>
      </div>
      <div class="thirdContent">
        <div class="thirdSection">
          <relations-dashboard
            :oneToOneCounter="80"
            :oneToMCounter="26"
            :mToNCounter="54"
          />
        </div>
        <div class="totalTime">
          <div class="subTitle">Total Time Taken :</div>
          <div class="timeValue">
            <span> 170.259 </span>
            <span>sec</span>
          </div>
        </div>
      </div>
      <div class="controlBtns">
        <button class="customBtn">Proceed</button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/Colors.scss";
@import "../scss/Button.scss";
.ipOutput {
  .content {
    padding: 25px;
  }
}
.subTitle {
  padding: 20px;
  font-size: 45px;
  font-weight: 700;
  font-family: "Indie Flower", cursive;
  text-align: center;
  color: $darkBlue;
}
.showStatistics {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 45px;
  margin-top: 45px;
  .firstSection,
  .secondSection {
    width: 100%;
  }
}
.thirdContent {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 45px;
  .thirdSection {
    width: 100%;
  }
  .totalTime {
    margin: auto;
    .timeValue {
      padding: 20px;
      font-size: 40px;
      font-weight: 700;
      text-align: center;
      color: $darkBlue;
    }
  }
}
.controlBtns {
  margin-top: 30px;
  text-align: center;
  .customBtn {
    width: 30%;
  }
}
@media screen and (max-width: 900px) {
  .showStatistics {
    grid-template-columns: 1fr;
  }
  .thirdContent {
    grid-template-columns: 1fr;
  }
}
@media screen and (max-width: 700px) {
  .controlBtns {
    .customBtn {
      width: 50%;
    }
  }
  .totalTime {
    .timeValue {
      padding: 10px;
      font-size: 30px;
    }
  }
}
</style>

<script>
import ipDashboard from "../components/ipDashboard.vue";
import datatypesDashboard from "../components/datatypesDashboard.vue";
import relationsDashboard from "../components/relationsDashboard.vue";
import showInfoTable from "../components/showInfoTable.vue";
export default {
  name: "ipOutput",
  components: {
    ipDashboard,
    datatypesDashboard,
    relationsDashboard,
    showInfoTable,
  },
};
</script>
