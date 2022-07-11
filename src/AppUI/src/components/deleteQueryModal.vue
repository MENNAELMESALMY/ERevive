<template>
  <div class="transparentBackground">
    <div class="popupBody">
      <i class="fa fa-times close" @click="closeModal"></i>
      <div class="content">
        <h1>Are you sure you want to delete "{{ this.queryName }}" ?</h1>
        <h3>{{ this.query }}</h3>
      </div>
      <div class="btn">
        <button class="customBtn" @click="deleteQuery">Delete</button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/GlobalPopup.scss";
@import "../scss/Colors.scss";
@import "../scss/Button.scss";
.popupBody {
  text-align: center;
  color: $darkBlue;
  width: 80%;
  .close {
    color: $darkBlue;
    &:hover {
      color: $lightBlue;
    }
  }
  h1 {
    border-bottom: 1px solid $lightGray;
    padding: 20px;
  }
  h3 {
    color: $lightBlue;
    padding: 20px;
    word-wrap: break-word;
  }
}
</style>

<script>
import { mapState } from "vuex";
export default {
  name: "deleteQueryModal",
  methods: {
    closeModal() {
      this.$store.commit("triggerModals/toggleDeleteQueryModal");
    },
    deleteQuery() {
      this.$store.commit("predictedQueries/deleteQuery", {
        query: this.query,
        queryName: this.queryName,
      });
      this.$store.commit("triggerModals/toggleDeleteQueryModal");
    },
  },
  computed: {
    ...mapState({
      query: (state) => state.predictedQueries.deletedQuery,
      queryName: (state) => state.predictedQueries.deletedQueryName,
    }),
  },
};
</script>
