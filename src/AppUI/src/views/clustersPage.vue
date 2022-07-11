<template>
  <div class="clustersPage">
    <div class="subTitle">Generated Clusters For Your System !</div>
    <cluster-card
      v-for="(cluster, i) in clusters"
      :key="i"
      :clusterName="cluster"
    />
    <div class="controlBtns">
      <button class="customBtn" @click="startApplication">Proceed</button>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/Colors.scss";
@import "../scss/Button.scss";

.clustersPage {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}
.subTitle {
  margin-top: 50px;
  padding: 20px;
  font-size: 45px;
  font-weight: 700;
  font-family: "Indie Flower", cursive;
  text-align: center;
  color: $darkBlue;
}
.controlBtns {
  width: 100%;
  text-align: center;
  .customBtn {
    width: 60%;
    margin: 12px;
  }
}
</style>

<script>
import { mapState } from "vuex";
import clusterCard from "../components/clusterCard.vue";
export default {
  name: "clustersPage",
  components: {
    clusterCard,
  },
  computed: {
    ...mapState({
      clusters: (state) => state.predictedQueries.clusters,
    }),
  },
  methods: {
    startApplication() {
      this.$store.dispatch("predictedQueries/postValidate");
    },
  },
};
</script>
