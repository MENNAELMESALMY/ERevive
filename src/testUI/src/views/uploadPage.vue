<template>
  <div class="uploadPage">
    <div class="subTitle">Step 1 Upload ER Diagram Image</div>
    <upload-image />
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/Colors.scss";
.subTitle {
  padding: 20px;
  font-size: 45px;
  font-weight: 700;
  font-family: "Indie Flower", cursive;
  text-align: center;
  color: $darkBlue;
}
</style>

<script>
import uploadImage from "../components/uploadImage.vue";
export default {
  name: "uploadPage",
  components: { uploadImage },
};
</script>
