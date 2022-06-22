
import { createWebHistory, createRouter } from "vue-router";
import home from "../views/home.vue";
import c1 from "../views/c1_view.vue";
import c2 from "../views/c2_view.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: home,
  },

		{
		path: "/c1",
		name: "c1",
		component: c1
		},

		{
		path: "/c2",
		name: "c2",
		component: c2
		},

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
    