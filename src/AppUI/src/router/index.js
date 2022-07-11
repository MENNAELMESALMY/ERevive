import Vue from "vue";
import VueRouter from "vue-router";
import home from "../views/homePage.vue";
import mainPage from "../views/mainPage.vue";
import uploadPage from "../views/uploadPage.vue";
import systemInfo from "../views/systemInfo.vue";
import ipOutput from "../views/ipOutput.vue";
import loadingPage from "../views/loadingPage.vue";
import validationPage from "../views/validationPage.vue";
import predictedQueriesPage from "../views/predictedQueriesPage.vue";
import clustersPage from "../views/clustersPage.vue";

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
      {
        path: "/ipOutput",
        name: "ipOutput",
        component: ipOutput,
        children: [],
      },
      {
        path: "/loadingPage",
        name: "loadingPage",
        component: loadingPage,
        children: [],
      },
      {
        path: "/validationPage",
        name: "validationPage",
        component: validationPage,
      },
      {
        path: "/predictedQueriesPage",
        name: "predictedQueriesPage",
        component: predictedQueriesPage,
        children: [],
      },
      {
        path: "/clustersPage",
        name: "clustersPage",
        component: clustersPage,
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