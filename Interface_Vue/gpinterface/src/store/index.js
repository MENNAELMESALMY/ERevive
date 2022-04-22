import Vue from "vue";
import Vuex from "vuex";
import colorPallete from "./modules/colorPallete";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    colorPallete,
  },
});
