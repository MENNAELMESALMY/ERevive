
//import * as Vue from "vue";
import Vuex from "vuex";
import posts_comments,_ from "./modules/posts_comments,_.js";
import writes__ from "./modules/writes__.js";


import color_pallete from "./modules/color_pallete.js";
//Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
	posts_comments,_,
	writes__,

    color_pallete
  },
});