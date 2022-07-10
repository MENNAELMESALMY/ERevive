<template>
  <div class="clusterCard">
    <router-link to="/predictedQueriesPage">
      <div class="cluster" @click="openClusterPage">
        <h1>{{ clusterName }}</h1>
      </div>
    </router-link>
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/Colors.scss";
.clusterCard {
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
  .cluster {
    text-align: center;
    width: 100%;
    h1 {
      font-size: 30px;
      font-weight: 700;
      color: $darkBlue;
    }
  }
}
a:hover {
  text-decoration: none;
}
</style>

<script>
export default {
  name: "clusterCard",
  props: {
    clusterName: {
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
