import Vue from "vue";
import VueRouter from "vue-router";
import home from "../views/homePage.vue";
import mainPage from "../views/mainPage.vue";
import uploadPage from "../views/uploadPage.vue";
import systemInfo from "../views/systemInfo.vue";

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
    children: [
      {
        path: "/systemInfo",
        name: "systemInfo",
        component: systemInfo,
        children: [],
      },
      {
        path: "/uploadPage",
        name: "uploadPage",
        component: uploadPage,
        children: [],
      },
    ],
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
