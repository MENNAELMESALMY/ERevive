import axios from "axios";
const state = {
  systemName: "",
  systemDescription: "",
  dataBaseName: "",
  dataBaseUserName: "",
  dataBasePassword: "",
};

const mutations = {
  setSystemInfo(state, systemObject) {
    state.systemName = systemObject.systemName;
    state.systemDescription = systemObject.systemDescription;
    state.dataBaseName = systemObject.dataBaseName;
    state.dataBaseUserName = systemObject.dataBaseUserName;
    state.dataBasePassword = systemObject.dataBasePassword;
  },
  setErImage(state, image) {
    state.erImage = image;
  },
};

const actions = {
  async postImage({ commit }, payload) {
    try {
      await axios.post("/imageprocessing", payload.image);
      commit("setErImage", payload.image);
    } catch (err) {
      console.log(err);
    }
  },
};
export default {
  namespaced: true,
  state,
  mutations,
  actions,
};
