////Demo file should be automated

const state = {
  endpoint_name: [
    {
      field1: "www",
      field2: "zzz",
    },
    {
      field1: "www22",
      field2: "zzz22",
    },
    {
      field1: "www33",
      field2: "zzz33",
    },
  ],
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
