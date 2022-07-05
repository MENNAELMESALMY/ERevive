<template>
  <div class="uploadImage">
    <form>
      <input type="file" name="file" @change="onFileChange()" />
      <button type="submit" @click="showImage()">Upload</button>
    </form>
  </div>
</template>

<style lang="scss" scoped></style>

<script>
export default {
  name: "uploadImage",
  data() {
    return {
      imageFile: null,
    };
  },
  methods: {
    onFileChange: function (event) {
      this.imageFile = event.target.files[0];
      if (this.imageFile) {
        const reader = new FileReader();
        var image = new Image();
        reader.addEventListener("load", function () {
          image.setAttribute("src", this.result);
        });
        reader.readAsDataURL(this.imageFile);
      }
    },
    showImage() {},
  },
};
</script>
