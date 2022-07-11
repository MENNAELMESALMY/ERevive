import Vue from "vue";
import Vuex from "vuex";
import controlSideBar from "./modules/controlSideBar.js";
import triggerModals from "./modules/triggerModals.js";
import predictedQueries from "./modules/predictedQueries.js";
import systemInput from "./modules/systemInput.js";
import validation from "./modules/validation";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    controlSideBar,
    triggerModals,
    predictedQueries,
    systemInput,
    validation,
  },
});
