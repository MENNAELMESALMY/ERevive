<template>
  <div class="ipOutput">
    <div class="content">
      <div class="subTitle">What we get from Image Processing !</div>
      <ip-dashboard
        :entitiesCounter="numEntities"
        :relationsCounter="numRelations"
        :attributesCounter="numAttributes"
      />
      <div class="showStatistics">
        <div class="firstSection">
          <datatypes-dashboard
            :stringTypePercent="stringPercent"
            :intTypePercent="intPercent"
            :floatTypePercent="floatPercent"
            :boolTypePercent="booleanPercent"
            :dateTypePercent="datePercent"
          />
        </div>
        <div class="secondSection">
          <show-info-table
            :primaryKeysCount="numPrimaryKeys"
            :multivaluedCount="numMultivalued"
            :identifyingCount="numIdentifying"
            :weakEntitiesCount="numWeakEntities"
            :naryCount="naryNum"
            :fullCount="fullNum"
            :partialCount="partialNum"
          />
        </div>
      </div>
      <div class="thirdContent">
        <div class="thirdSection">
          <relations-dashboard
            :oneToOneCounter="numOneToOne"
            :oneToMCounter="numOneToMany"
            :mToNCounter="numManyToMany"
          />
        </div>
        <div class="totalTime">
          <div class="subTitle">Total Time Taken :</div>
          <div class="timeValue">
            <span> {{ totalTime }} </span>
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
import { mapState } from "vuex";
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
  computed: {
    ...mapState({
      numEntities: (state) => state.systemInput.numEntities,
      numRelations: (state) => state.systemInput.numRelations,
      numAttributes: (state) => state.systemInput.numAttributes,
      stringPercent: (state) => state.systemInput.stringPercent,
      intPercent: (state) => state.systemInput.intPercent,
      floatPercent: (state) => state.systemInput.floatPercent,
      booleanPercent: (state) => state.systemInput.booleanPercent,
      datePercent: (state) => state.systemInput.datePercent,
      numPrimaryKeys: (state) => state.systemInput.numPrimaryKeys,
      numMultivalued: (state) => state.systemInput.numMultivalued,
      numIdentifying: (state) => state.systemInput.numIdentifying,
      numWeakEntities: (state) => state.systemInput.numWeakEntities,
      naryNum: (state) => state.systemInput.naryNum,
      fullNum: (state) => state.systemInput.fullNum,
      partialNum: (state) => state.systemInput.partialNum,
      numOneToOne: (state) => state.systemInput.numOneToOne,
      numOneToMany: (state) => state.systemInput.numOneToMany,
      numManyToMany: (state) => state.systemInput.numManyToMany,
      totalTime: (state) => state.systemInput.totalTime,
    }),
  },
};
</script>
