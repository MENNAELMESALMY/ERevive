<template>
  <div class="uploadImage">
    <div class="container">
      <div class="wrapper">
        <div class="image">
          <img id="uploadedImage" src="" alt="image" />
        </div>
        <div class="content">
          <div class="icon"><i class="fa fa-cloud-upload"></i></div>
          <div class="text">No File Chosen, Yet!</div>
        </div>
      </div>
    </div>
    <div class="controlBtns">
      <input id="default-btn" type="file" hidden />
      <button class="customBtn" @click="uploadImageFile()">Upload Image</button>
      <button class="customBtn" @click="processImage()">Proceed</button>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/Colors.scss";
@import "../scss/Button.scss";
.uploadImage {
  display: grid;
  height: 87vh;
  place-items: center;
  text-align: center;
}
.container {
  height: calc(100vh - 300px);
  width: 70%;
  .wrapper {
    position: relative;
    height: 100%;
    width: 100%;
    border-radius: 10px;
    background-color: $lightGray;
    border: 2px dashed #c2cdda;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    .image {
      position: absolute;
      height: 100%;
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      img {
        height: 100%;
        width: 100%;
        display: none;
      }
    }
    .icon {
      font-size: 100px;
      color: $lightYellow;
    }
    .text {
      font-size: 20px;
      font-weight: 500;
      color: white;
    }
  }
}
.controlBtns {
  margin-top: 25px;
  width: 100%;
  padding-top: 20px;
  padding-right: 20px;
  margin-bottom: 25px;
  border-top: 1px solid #c2cdda;
  display: flex;
  justify-content: flex-end;
  .customBtn {
    margin-left: 12px;
  }
}
@media screen and (max-width: 768px) {
  .container {
    width: 90%;
  }
  .controlBtns {
    justify-content: center;
    flex-wrap: wrap;
    padding-right: 10px;
  }
  .customBtn {
    margin-top: 12px;
  }
}
</style>

<script>
import { mapState } from "vuex";
export default {
  name: "uploadImage",
  data() {
    return {
      imageUploaded: false,
    };
  },
  computed: {
    ...mapState({
      ipOutPutReturned: (state) => state.systemInput.ipOutPutReturned,
    }),
  },
  methods: {
    // onFileChange: function (event) {
    //   this.imageFile = event.target.files[0];
    //   if (this.imageFile) {
    //     const reader = new FileReader();
    //     var image = new Image();
    //     reader.addEventListener("load", function () {
    //       image.setAttribute("src", this.result);
    //     });
    //     reader.readAsDataURL(this.imageFile);
    //   }
    // },
    uploadImageFile() {
      const inputFieldBtn = document.getElementById("default-btn");
      const image = document.getElementById("uploadedImage");
      inputFieldBtn.click();
      inputFieldBtn.onchange = function () {
        image.setAttribute("src", URL.createObjectURL(inputFieldBtn.files[0]));
        image.style.display = "block";
      };
      this.imageUploaded = true;
    },
    async getImageBlob(imageUrl) {
      const response = await fetch(imageUrl);
      return response.blob();
    },
    async processImage() {
      if (this.imageUploaded) {
        this.$store.commit(
          "predictedQueries/setLoadingTitle",
          "Image Processing is Running ..."
        );
        this.$router.push("/loadingPage");
        const image = document.getElementById("uploadedImage");
        let imageBlob = await this.getImageBlob(image.src);
        console.log(imageBlob);
        let imageName =
          image.src.split("/")[image.src.split("/").length - 1] +
          "." +
          imageBlob.type.split("/")[1];
        const formData = new FormData();
        formData.append("image", imageBlob, imageName);

        this.$store.dispatch("systemInput/postImage", formData);
        this.interval = setInterval(() => {
          this.$store.dispatch("systemInput/getIpOutput");
          if (this.ipOutPutReturned) {
            clearInterval(this.interval);
          }
        }, 10000);
      } else {
        alert("Please upload an image first!");
      }
    },
  },
};
</script>
