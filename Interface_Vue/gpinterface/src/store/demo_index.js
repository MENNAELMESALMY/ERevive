import Vue from "vue";
import Vuex from "vuex";
import employee from "./modules/employee_store.vue";
import student from "./modules/student_store.vue";
import teacher from "./modules/teacher_store.vue";
import admin from "./modules/admin_store.vue";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    employee,
    student,
    teacher,
    admin,
  },
});
