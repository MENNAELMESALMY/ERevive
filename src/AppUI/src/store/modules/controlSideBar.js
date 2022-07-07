const state = {
  moveToHome: false,
  moveToSql: false,
  moveToApi: false,
  moveToFront: false,
  moveToSchema: false,
};

const mutations = {
  toggleMoveToHome(state) {
    state.moveToHome = !state.moveToHome;
  },
  toggleMoveToSql(state) {
    state.moveToSql = !state.moveToSql;
  },
  toggleMoveToApi(state) {
    state.moveToApi = !state.moveToApi;
  },
  toggleMoveToFront(state) {
    state.moveToFront = !state.moveToFront;
  },
  toggleMoveToSchema(state) {
    state.moveToSchema = !state.moveToSchema;
  },
};
export default {
  namespaced: true,
  state,
  mutations,
};
