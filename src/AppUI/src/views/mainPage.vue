<template>
  <div class="mainPage">
    <div class="sideBar">
      <img
        src="../../public/assets/home.png"
        alt="homeIcon"
        @click="routeToPage('homePage')"
      />
      <img
        src="../../public/assets/sql.png"
        alt="sqlIcon"
        @click="routeToPage('database')"
      />
      <img
        src="../../public/assets/api.png"
        alt="apiIcon"
        @click="routeToPage('api')"
      />
      <img
        src="../../public/assets/frontDemo.png"
        alt="frontIcon"
        @click="routeToPage('front')"
      />
      <img
        src="../../public/assets/schema.png"
        alt="schemaIcon"
        @click="routeToPage('schemaPage')"
      />
      <img
        src="../../public/assets/nlp.png"
        alt="nlpIcon"
        @click="routeToPage('nlpToSqlPage')"
      />
    </div>
    <div class="mainContent">
      <savedModal v-if="savedModalState" />
      <delete-query-modal v-if="deleteQueryModalState" />
      <add-query-modal v-if="addQueryModalState" />
      <router-view />
    </div>
  </div>
</template>

<style lang="scss" scoped>
.mainPage {
  display: flex;
  flex-direction: row;
}
@import "../scss/Colors.scss";
.sideBar {
  width: 100px;
  min-height: 100vh;
  background-color: $darkBlue;
  text-align: center;
  img {
    width: 70px;
    padding: 15px;
    cursor: pointer;
  }
}
.mainContent {
  width: 100%;
}
</style>

<script>
import { mapState } from "vuex";
import AddQueryModal from "../components/addQueryModal.vue";
import DeleteQueryModal from "../components/deleteQueryModal.vue";
import savedModal from "../components/savedModal.vue";
export default {
  name: "mainPage",
  components: {
    savedModal,
    DeleteQueryModal,
    AddQueryModal,
  },
  computed: {
    ...mapState({
      savedModalState: (state) => state.triggerModals.savedModal,
      deleteQueryModalState: (state) => state.triggerModals.deleteQueryModal,
      addQueryModalState: (state) => state.triggerModals.addQueryModal,
      appFinished: (state) => state.predictedQueries.appFinished,
    }),
  },
  methods: {
    routeToPage(page) {
      if (this.appFinished) {
        if (page == "homePage") {
          this.$router.push("/");
        } else if (page == "database") {
          this.$router.push("/databaseSeeds");
        } else if (page == "api") {
          window.open("http://localhost:3000/", "_blank");
        } else if (page == "front") {
          window.open("http://localhost:8081/", "_blank");
        } else if (page == "schemaPage") {
          this.$router.push("/schemaPage");
        } else if (page == "nlpToSqlPage") {
          this.$router.push("/nlpToSqlPage");
        }
      }
    },
  },
};
</script>
