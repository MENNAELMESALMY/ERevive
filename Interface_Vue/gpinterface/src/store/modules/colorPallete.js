const state = {
  themeColor: "#f90",
};

const mutations = {
  setThemeColor(state, color) {
    state.themeColor = color;
  },
};

const getters = {
  themeColor: (state) => state.themeColor,
};

export default {
  state,
  mutations,
  getters,
};
