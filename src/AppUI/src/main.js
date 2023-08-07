import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

Vue.config.productionTip = false;
// set axios global config
import axios from "axios";
axios.defaults.baseURL = "http://localhost:5000/";

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
