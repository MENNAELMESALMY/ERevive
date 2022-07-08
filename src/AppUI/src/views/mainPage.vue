<template>
  <div class="mainPage">
    <div class="sideBar">
      <img src="../../public/assets/home.png" alt="homeIcon" />
      <img src="../../public/assets/sql.png" alt="sqlIcon" />
      <img src="../../public/assets/api.png" alt="apiIcon" />
      <img src="../../public/assets/frontDemo.png" alt="frontIcon" />
      <img src="../../public/assets/schema.png" alt="schemaIcon" />
    </div>
    <div class="mainContent">
      <savedModal v-if="savedModalState" />
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
import savedModal from "../components/savedModal.vue";
export default {
  name: "mainPage",
  components: {
    savedModal,
  },
  computed: {
    ...mapState({
      savedModalState: (state) => state.triggerSavedModal.savedModal,
    }),
  },
};
</script>
