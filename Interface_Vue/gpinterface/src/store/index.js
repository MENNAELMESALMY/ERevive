
import Vue from "vue";
import Vuex from "vuex";
import c1 from "./modules/c1_store.vue";
import c2 from "./modules/c2_store.vue";


Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
	c1,
	c2,

  },
});