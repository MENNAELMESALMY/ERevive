
//import * as Vue from "vue";
import Vuex from "vuex";
import employee from "./modules/employee.js";
import dependent from "./modules/dependent.js";
import department_location from "./modules/department_location.js";
import works_employee_project from "./modules/works_employee_project.js";
import employee_department_location_department from "./modules/employee_department_location_department.js";


import color_pallete from "./modules/color_pallete.js";
//Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
	employee,
	dependent,
	department_location,
	works_employee_project,
	employee_department_location_department,

    color_pallete
  },
});