<template>
  <div class="transparentBackground">
    <div class="popupBody">
      <i class="fa fa-times close" @click="closeModal"></i>
      <div class="content">
        <h1>System Information</h1>
        <h3>Saved Successfully !</h3>
      </div>
      <div class="btn">
        <router-link to="/uploadPage">
          <button class="customBtn" @click="closeModal">Proceed</button>
        </router-link>
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
  }
}
a:hover {
  text-decoration: none;
}
</style>

<script>
export default {
  name: "savedModal",
  methods: {
    closeModal() {
      this.$store.commit("triggerModals/toggleSavedModal");
    },
  },
};
</script>
