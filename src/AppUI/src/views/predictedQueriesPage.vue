<template>
  <div class="predictedQueriesPage">
    <div class="subTitle">Predicted Queries For Your System !</div>
    <div class="subTitleCluster">{{ currentClusterName }}</div>
    <div class="content">
      <queries-card
        v-for="(query, i) in queries"
        :key="i"
        :query="query.query"
        :queryName="query.name"
        :id="i.toString()"
      />
      <div class="emptyQueries" v-if="queries.length == 0">
        <img src="../../public/assets/box.png" alt="emptyBox" />
        <p class="subTitle">OOPS ! No Predicted Queries Found</p>
      </div>
    </div>
    <div class="controlBtns">
      <button class="customBtn" @click="toggleAddQueryModal">
        Add New Query
      </button>
      <button
        class="customBtn"
        v-if="queries.length > 0"
        @click="startApplication"
      >
        Proceed
      </button>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/Colors.scss";
@import "../scss/Button.scss";
.subTitle,
.subTitleCluster {
  margin-top: 50px;
  padding: 20px;
  font-size: 45px;
  font-weight: 700;
  font-family: "Indie Flower", cursive;
  text-align: center;
  color: $darkBlue;
}
.subTitleCluster {
  margin-top: 0px;
  padding-top: 0px;
}
.content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}
.controlBtns {
  display: flex;
  justify-content: center;
  flex-direction: row;
  margin-top: 20px;
  margin-bottom: 12px;
  text-align: center;
  .customBtn {
    width: 30%;
    margin: 12px;
  }
}
.emptyQueries {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
@media screen and (max-width: 900px) {
  .controlBtns {
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: 10px;
    .customBtn {
      width: 80%;
    }
  }
  .emptyQueries {
    img {
      width: 200px;
      height: 200px;
    }
    .subTitle {
      font-size: 25px;
    }
  }
}
</style>

<script>
import { mapState } from "vuex";
import queriesCard from "../components/queriesCard.vue";
export default {
  name: "predictedQueriesPage",
  components: {
    queriesCard,
  },
  computed: {
    ...mapState({
      queries: (state) => state.predictedQueries.queries,
      currentClusterName: (state) => state.predictedQueries.currentClusterName,
    }),
  },
  methods: {
    toggleAddQueryModal() {
      this.$store.commit("triggerModals/toggleAddQueryModal");
    },
    startApplication() {
      this.$store.dispatch("predictedQueries/postStartApplication");
      this.$store.commit(
        "systemInput/setLoadingTitle",
        "Creating Application ..."
      );
      this.$router.push("/loadingPage");
    },
  },
};
</script>
