
//import * as Vue from "vue";
import Vuex from "vuex";
import c1 from "./modules/c1.js";
import c2 from "./modules/c2.js";


import color_pallete from "./modules/color_pallete.js";
//Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
	c1,
	c2,

    color_pallete
  },
});