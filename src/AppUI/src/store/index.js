import Vue from "vue";
import Vuex from "vuex";
import controlSideBar from "./modules/controlSideBar.js";
import triggerSavedModal from "./modules/triggerSavedModal";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    controlSideBar,
    triggerSavedModal,
  },
});
