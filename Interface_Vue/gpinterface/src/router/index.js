
import Vue from "vue";
import VueRouter from "vue-router";
import home from "../views/home_view.vue";
import c1 from "../views/c1_view.vue";
import c2 from "../views/c2_view.vue";


Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: home,
    children: [

		{
		path: "c1/",
		name: "c1",
		component: c1
		},

		{
		path: "c2/",
		name: "c2",
		component: c2
		},

    ]
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
    