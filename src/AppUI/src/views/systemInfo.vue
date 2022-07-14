<template>
  <div class="systemInfo">
    <div class="title">
      <h1>Let's Know More About Your System !</h1>
    </div>
    <div>
      <form @submit.prevent="submitForm">
        <div class="inputs">
          <input
            type="text"
            id="systemName"
            placeholder="Enter System Name"
            v-model="systemName"
            required
          />
          <input
            type="text"
            id="systemDescription"
            placeholder="Enter System Description"
            v-model="systemDescription"
            required
          />
          <input
            type="text"
            id="username"
            placeholder="Enter Database Username"
            v-model="username"
            required
          />
          <input
            type="password"
            id="password"
            placeholder="Enter Database Password"
            v-model="password"
            required
          />
          <input
            type="text"
            id="databaseName"
            placeholder="Enter Database Name"
            v-model="databaseName"
            required
          />
        </div>
        <div class="controlBtns">
          <input
            type="submit"
            class="customBtn"
            value="Submit"
            id="submitbuttonId"
          />
        </div>
      </form>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/Colors.scss";
@import "../scss/Button.scss";
.systemInfo {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  color: white;
  font-size: 30px;
  font-weight: 700;
  padding: 15px;
  padding-top: 30px;
  padding-bottom: 30px;
}
.title {
  width: 100%;
  text-align: center;
  margin-top: 50px;
  padding: 15px;
  padding-top: 30px;
  padding-bottom: 30px;
  h1 {
    font-weight: 700;
    font-size: 45px;
    font-family: "Indie Flower", cursive;
    color: $darkBlue;
  }
}
form {
  display: flex;
  justify-content: center;
  flex-direction: column;
}
.inputs {
  width: 100%;
  input {
    width: 100%;
    margin-bottom: 35px;
    padding: 10px;
    border: none;
    border-bottom: 2px solid $darkBlue;
    font-size: 27px;
    font-family: "Indie Flower", cursive;
    font-weight: 700;
    color: $darkBlue;
    &:focus {
      outline: none;
      border-bottom: 2px solid $lightBlue;
    }
  }
}
.controlBtns {
  margin-top: 30px;
  text-align: center;
}
.customBtn {
  margin-right: 12px;
  width: 30%;
}
@media screen and (max-width: 768px) {
  .customBtn {
    margin-right: 0px;
    margin-top: 12px;
    width: 90%;
  }
}
</style>

<script>
export default {
  name: "systemInfo",
  data() {
    return {
      systemName: "",
      systemDescription: "",
      username: "",
      password: "",
      databaseName: "",
    };
  },
  mounted() {
    this.$store.commit("triggerModals/setHeaderModal", "System Information");
    this.$store.commit("triggerModals/setToPageFromModal", "/uploadPage");
  },
  methods: {
    submitForm() {
      // this.$store.commit("triggerModals/toggleSavedModal");
      this.$store.commit("predictedQueries/setSystemInfo", {
        systemName: this.systemName,
        systemDescription: this.systemDescription,
        databaseUsername: this.username,
        databasePassword: this.password,
        databaseName: this.databaseName,
      });
      this.$router.push("/uploadPage");
    },
  },
};
</script>
