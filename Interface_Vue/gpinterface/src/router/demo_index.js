import Vue from "vue";
import VueRouter from "vue-router";
import home from "../views/home_view.vue";
import employee from "../views/employee_view.vue";
import student from "../views/student_view.vue";
import teacher from "../views/teacher_view.vue";
import admin from "../views/admin_view.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: home,
    children: [
      {
        path: "employee/",
        name: "employee",
        component: employee,
      },

      {
        path: "student/",
        name: "student",
        component: student,
      },

      {
        path: "teacher/",
        name: "teacher",
        component: teacher,
      },

      {
        path: "admin/",
        name: "admin",
        component: admin,
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
