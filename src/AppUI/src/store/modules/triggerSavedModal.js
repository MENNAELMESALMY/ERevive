const state = {
  savedModal: false,
};

const mutations = {
  toggleSavedModal(state) {
    state.savedModal = !state.savedModal;
  },
};
export default {
  namespaced: true,
  state,
  mutations,
};
