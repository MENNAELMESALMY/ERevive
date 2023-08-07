<template>
  <div class="queriesErrosCard">
    <router-link to="/predictedQueriesPage">
      <div class="error" @click="openClusterPage">
        <h1>{{ clusterName }}</h1>
        <p>{{ clusterQuery }}</p>
      </div>
    </router-link>
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/Colors.scss";
.queriesErrosCard {
  width: 80%;
  margin: 30px;
  padding: 20px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease 0s;
  &:hover {
    transform: translateY(-3px);
  }
  .error {
    width: 100%;
    h1 {
      font-size: 30px;
      font-weight: 700;
      color: $darkBlue;
    }
    p {
      font-size: 25px;
      color: $darkBlue;
      word-wrap: break-word;
    }
  }
}
a:hover {
  text-decoration: none;
}
</style>

<script>
export default {
  name: "queriesErrorsCard",
  props: {
    clusterName: {
      type: String,
      required: true,
    },
    clusterQuery: {
      type: String,
      required: true,
    },
  },
  methods: {
    openClusterPage() {
      this.$store.commit(
        "predictedQueries/setCurrentCluster",
        this.clusterName
      );
    },
  },
};
</script>
