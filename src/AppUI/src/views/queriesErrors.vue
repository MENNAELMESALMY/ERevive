<template>
  <div class="queriesErrors">
    <div class="subTitle">Sorry Invalid Queries Detected !</div>
    <div v-for="(cluster, i) in errorsClusters" :key="i">
      <queries-errors-card
        v-for="(query, j) in queriesErrors[cluster]"
        :key="j"
        :clusterName="cluster"
        :clusterQuery="query[0].query"
      />
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/Colors.scss";
.queriesErrors {
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
</style>

<script>
import { mapState } from "vuex";
import queriesErrorsCard from "../components/queriesErrorsCard.vue";
export default {
  name: "queriesErrors",
  components: {
    queriesErrorsCard,
  },
  computed: {
    ...mapState({
      errorsClusters: (state) => state.predictedQueries.errorsClusters,
      queriesErrors: (state) => state.predictedQueries.queriesErrors,
    }),
  },
};
</script>
