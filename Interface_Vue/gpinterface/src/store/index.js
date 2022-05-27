import Vue from "vue";
import Vuex from "vuex";
import colorPallete from "./modules/colorPallete";
import cluster_name from "./modules/cluster_name";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    colorPallete,
    cluster_name,
  },
});
