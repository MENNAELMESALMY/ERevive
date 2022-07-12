const state = {
  savedModal: false,
  deleteQueryModal: false,
  addQueryModal: false,
  headerModal: "System Information",
  toPageFromModal: "/uploadPage",
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
  setHeaderModal(state, header) {
    state.headerModal = header;
  },
  setToPageFromModal(state, page) {
    state.toPageFromModal = page;
  },
};
export default {
  namespaced: true,
  state,
  mutations,
};
