<template>
  <div class="transparentBackground">
    <div class="popupBody">
      <i class="fa fa-times close" @click="closeModal"></i>
      <div class="content">
        <h1>Add New Query !</h1>
        <div class="addQuery">
          <form @submit.prevent="addNewQuery">
            <input
              type="text"
              placeholder="Query Name"
              v-model="newQueryName"
              required
            />
            <textarea
              v-model="newQuery"
              placeholder="Write Your Query Here ..."
              required
            ></textarea>
            <div class="btn">
              <input type="submit" class="customBtn" value="Done" />
            </div>
          </form>
        </div>
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
    padding: 20px;
  }
}
.addQuery {
  form {
    input {
      width: 100%;
      margin-bottom: 35px;
      padding: 10px;
      border: none;
      border-bottom: 2px solid $darkBlue;
      font-size: 27px;
      font-weight: 700;
      color: $darkBlue;
      &:focus {
        outline: none;
        border-bottom: 2px solid $lightBlue;
      }
    }
    textarea {
      padding: 12px;
      font-size: 22px;
      width: 100%;
      max-width: 100%;
      min-height: 200px;
      color: $darkBlue;
      border: 1px solid $darkBlue;
      &:focus {
        outline: none;
        border: 2px solid $lightBlue;
      }
    }
    .btn {
      margin-top: 25px;
      width: 80%;
      .customBtn {
        color: white;
      }
    }
  }
}
</style>

<script>
export default {
  name: "addQueryModal",
  data() {
    return {
      newQuery: "",
      newQueryName: "",
    };
  },
  methods: {
    closeModal() {
      this.$store.commit("triggerModals/toggleAddQueryModal");
    },
    addNewQuery() {
      if (this.newQueryName != "" && this.newQuery != "") {
        this.$store.commit("predictedQueries/addNewQuery", {
          queryName: this.newQueryName,
          query: this.newQuery,
        });
        this.$store.commit("triggerModals/toggleAddQueryModal");
      }
    },
  },
};
</script>
