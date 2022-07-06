import Vue from "vue";
import VueRouter from "vue-router";
import home from "../views/homePage.vue";
import mainPage from "../views/mainPage.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: home,
    children: [],
  },
  {
    path: "/mainPage",
    name: "mainPage",
    component: mainPage,
    children: [],
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
