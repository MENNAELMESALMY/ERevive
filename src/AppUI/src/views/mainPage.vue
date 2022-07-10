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
    }),
  },
};
</script>
