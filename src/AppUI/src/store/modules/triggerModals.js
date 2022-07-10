const state = {
  savedModal: false,
  deleteQueryModal: false,
  addQueryModal: false,
};

const mutations = {
  toggleSavedModal(state) {
    state.savedModal = !state.savedModal;
  },
  toggleDeleteQueryModal(state) {
    state.deleteQueryModal = !state.deleteQueryModal;
  },
  toggleAddQueryModal(state) {
    state.addQueryModal = !state.addQueryModal;
  },
};
export default {
  namespaced: true,
  state,
  mutations,
};
