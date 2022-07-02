
import { createWebHistory, createRouter } from "vue-router";
import home from "../views/home.vue";
import main_page from "../views/main_page.vue";
import get_employee_filteredby_sex_salary from "../components/get_employee_filteredby_sex_salary.vue";
import get_works_employee_project_filteredby_project_name from "../components/get_works_employee_project_filteredby_project_name.vue";
import get_dependent_groupedby_all from "../components/get_dependent_groupedby_all.vue";
import get_employee_filteredby_last_name_orderedby_employee_supervision_ssn from "../components/get_employee_filteredby_last_name_orderedby_employee_supervision_ssn.vue";
import get_employee_filteredby_last_name_groupedby_all_orderedby_salary from "../components/get_employee_filteredby_last_name_groupedby_all_orderedby_salary.vue";
import get_employee_filteredby_salary_groupedby_birth_date_orderedby_salary from "../components/get_employee_filteredby_salary_groupedby_birth_date_orderedby_salary.vue";
import get_employee_groupedby_last_name_orderedby_all from "../components/get_employee_groupedby_last_name_orderedby_all.vue";
import get_employee_filteredby_employee_supervision_ssn_groupedby_salary_middle_name_last_name_employee_supervision_ssn from "../components/get_employee_filteredby_employee_supervision_ssn_groupedby_salary_middle_name_last_name_employee_supervision_ssn.vue";
import get_employee_orderedby_all from "../components/get_employee_orderedby_all.vue";
import get_employee_groupedby_salary_last_name_orderedby_all from "../components/get_employee_groupedby_salary_last_name_orderedby_all.vue";
import get_employee_groupedby_last_name_employee_supervision_ssn_orderedby_all from "../components/get_employee_groupedby_last_name_employee_supervision_ssn_orderedby_all.vue";
import get_employee_department_location_department_filteredby_department_name_groupedby_middle_name_address_department_name_last_name from "../components/get_employee_department_location_department_filteredby_department_name_groupedby_middle_name_address_department_name_last_name.vue";
import create_department_location from "../components/create_department_location.vue";
import get_employee_groupedby_all from "../components/get_employee_groupedby_all.vue";
import get_employee_groupedby_address_orderedby_all from "../components/get_employee_groupedby_address_orderedby_all.vue";
import get_employee_filteredby_salary_orderedby_salary from "../components/get_employee_filteredby_salary_orderedby_salary.vue";
import get_employee_filteredby_last_name_groupedby_birth_date from "../components/get_employee_filteredby_last_name_groupedby_birth_date.vue";
import get_employee_filteredby_birth_date_groupedby_birth_date from "../components/get_employee_filteredby_birth_date_groupedby_birth_date.vue";
import get_employee_groupedby_sex_orderedby_all from "../components/get_employee_groupedby_sex_orderedby_all.vue";
import get_works_employee_project_groupedby_all from "../components/get_works_employee_project_groupedby_all.vue";
import get_employee_department_location_department_filteredby_department_name_groupedby_middle_name_last_name_department_name from "../components/get_employee_department_location_department_filteredby_department_name_groupedby_middle_name_last_name_department_name.vue";
import get_works_employee_project_filteredby_project_name_groupedby_all from "../components/get_works_employee_project_filteredby_project_name_groupedby_all.vue";
import get_employee_department_location_department_groupedby_department_name_orderedby_employee_supervision_ssn from "../components/get_employee_department_location_department_groupedby_department_name_orderedby_employee_supervision_ssn.vue";
import get_employee_filteredby_salary_orderedby_employee_supervision_ssn from "../components/get_employee_filteredby_salary_orderedby_employee_supervision_ssn.vue";
import get_employee_filteredby_last_name_orderedby_salary from "../components/get_employee_filteredby_last_name_orderedby_salary.vue";
import get_employee_filteredby_last_name_birth_date_groupedby_employee_supervision_ssn_salary_birth_date from "../components/get_employee_filteredby_last_name_birth_date_groupedby_employee_supervision_ssn_salary_birth_date.vue";
import get_employee_filteredby_salary_groupedby_birth_date_salary_employee_supervision_ssn from "../components/get_employee_filteredby_salary_groupedby_birth_date_salary_employee_supervision_ssn.vue";
import get_employee_groupedby_salary_orderedby_all from "../components/get_employee_groupedby_salary_orderedby_all.vue";
import get_employee_filteredby_first_name_groupedby_all from "../components/get_employee_filteredby_first_name_groupedby_all.vue";
import get_employee_filteredby_salary_groupedby_birth_date_orderedby_employee_supervision_ssn from "../components/get_employee_filteredby_salary_groupedby_birth_date_orderedby_employee_supervision_ssn.vue";
import get_employee_groupedby_birth_date_orderedby_employee_supervision_ssn from "../components/get_employee_groupedby_birth_date_orderedby_employee_supervision_ssn.vue";
import get_employee_filteredby_last_name_groupedby_all from "../components/get_employee_filteredby_last_name_groupedby_all.vue";
import get_employee_groupedby_all_orderedby_birth_date from "../components/get_employee_groupedby_all_orderedby_birth_date.vue";
import get_employee_filteredby_sex_groupedby_all from "../components/get_employee_filteredby_sex_groupedby_all.vue";
import get_employee_department_location_department from "../components/get_employee_department_location_department.vue";
import get_employee_groupedby_middle_name_last_name_orderedby_all from "../components/get_employee_groupedby_middle_name_last_name_orderedby_all.vue";
import get_department_location from "../components/get_department_location.vue";
import get_employee_orderedby_status from "../components/get_employee_orderedby_status.vue";
import get_employee_filteredby_last_name_groupedby_birth_date_orderedby_salary from "../components/get_employee_filteredby_last_name_groupedby_birth_date_orderedby_salary.vue";
import get_dependent_filteredby_sex from "../components/get_dependent_filteredby_sex.vue";
import get_employee_filteredby_last_name_groupedby_birth_date_orderedby_employee_supervision_ssn from "../components/get_employee_filteredby_last_name_groupedby_birth_date_orderedby_employee_supervision_ssn.vue";
import get_employee_filteredby_salary_groupedby_birth_date_orderedby_birth_date from "../components/get_employee_filteredby_salary_groupedby_birth_date_orderedby_birth_date.vue";
import get_employee_filteredby_middle_name from "../components/get_employee_filteredby_middle_name.vue";
import get_employee_groupedby_salary_middle_name_last_name from "../components/get_employee_groupedby_salary_middle_name_last_name.vue";
import get_employee_groupedby_sex_orderedby_sex from "../components/get_employee_groupedby_sex_orderedby_sex.vue";
import get_employee_filteredby_first_name_middle_name_last_name_groupedby_middle_name from "../components/get_employee_filteredby_first_name_middle_name_last_name_groupedby_middle_name.vue";
import get_employee_filteredby_salary_groupedby_all from "../components/get_employee_filteredby_salary_groupedby_all.vue";
import get_employee_groupedby_employee_supervision_ssn_orderedby_all from "../components/get_employee_groupedby_employee_supervision_ssn_orderedby_all.vue";
import get_employee_filteredby_middle_name_last_name_groupedby_all from "../components/get_employee_filteredby_middle_name_last_name_groupedby_all.vue";
const routes = [
  {
    path: "/",
    name: "home",
    component: home,
  },
  {
    path: "/App",
    name: "App",
    component: main_page,
    children:[
    
        {
        
        path: "employee/get_employee_filteredby_middle_name_last_name_groupedby_all",
        name: "get_employee_filteredby_middle_name_last_name_groupedby_all",
        component: get_employee_filteredby_middle_name_last_name_groupedby_all,
        
        },
        
        {
        
        path: "employee/get_employee_filteredby_first_name_groupedby_all",
        name: "get_employee_filteredby_first_name_groupedby_all",
        component: get_employee_filteredby_first_name_groupedby_all,
        
        },
        
        {
        
        path: "employee/get_employee_filteredby_last_name_groupedby_all_orderedby_salary",
        name: "get_employee_filteredby_last_name_groupedby_all_orderedby_salary",
        component: get_employee_filteredby_last_name_groupedby_all_orderedby_salary,
        
        },
        
        {
        
        path: "employee/get_employee_filteredby_last_name_groupedby_all",
        name: "get_employee_filteredby_last_name_groupedby_all",
        component: get_employee_filteredby_last_name_groupedby_all,
        
        },
        
        {
        
        path: "employee/get_employee_filteredby_last_name_orderedby_salary",
        name: "get_employee_filteredby_last_name_orderedby_salary",
        component: get_employee_filteredby_last_name_orderedby_salary,
        
        },
        
        {
        
        path: "employee/get_employee_filteredby_sex_groupedby_all",
        name: "get_employee_filteredby_sex_groupedby_all",
        component: get_employee_filteredby_sex_groupedby_all,
        
        },
        
        {
        
        path: "employee/get_employee_orderedby_status",
        name: "get_employee_orderedby_status",
        component: get_employee_orderedby_status,
        
        },
        
        {
        
        path: "employee/get_employee_filteredby_salary_groupedby_all",
        name: "get_employee_filteredby_salary_groupedby_all",
        component: get_employee_filteredby_salary_groupedby_all,
        
        },
        
        {
        
        path: "employee/get_employee_filteredby_middle_name",
        name: "get_employee_filteredby_middle_name",
        component: get_employee_filteredby_middle_name,
        
        },
        
        {
        
        path: "employee/get_employee_groupedby_all",
        name: "get_employee_groupedby_all",
        component: get_employee_groupedby_all,
        
        },
        
        {
        
        path: "employee/get_employee_groupedby_all_orderedby_birth_date",
        name: "get_employee_groupedby_all_orderedby_birth_date",
        component: get_employee_groupedby_all_orderedby_birth_date,
        
        },
        
        {
        
        path: "employee/get_employee_filteredby_employee_supervision_ssn_groupedby_salary_middle_name_last_name_employee_supervision_ssn",
        name: "get_employee_filteredby_employee_supervision_ssn_groupedby_salary_middle_name_last_name_employee_supervision_ssn",
        component: get_employee_filteredby_employee_supervision_ssn_groupedby_salary_middle_name_last_name_employee_supervision_ssn,
        
        },
        
        {
        
        path: "employee/get_employee_groupedby_salary_middle_name_last_name",
        name: "get_employee_groupedby_salary_middle_name_last_name",
        component: get_employee_groupedby_salary_middle_name_last_name,
        
        },
        
        {
        
        path: "employee/get_employee_groupedby_salary_last_name_orderedby_all",
        name: "get_employee_groupedby_salary_last_name_orderedby_all",
        component: get_employee_groupedby_salary_last_name_orderedby_all,
        
        },
        
        {
        
        path: "employee/get_employee_groupedby_middle_name_last_name_orderedby_all",
        name: "get_employee_groupedby_middle_name_last_name_orderedby_all",
        component: get_employee_groupedby_middle_name_last_name_orderedby_all,
        
        },
        
        {
        
        path: "employee/get_employee_groupedby_last_name_employee_supervision_ssn_orderedby_all",
        name: "get_employee_groupedby_last_name_employee_supervision_ssn_orderedby_all",
        component: get_employee_groupedby_last_name_employee_supervision_ssn_orderedby_all,
        
        },
        
        {
        
        path: "employee/get_employee_groupedby_last_name_orderedby_all",
        name: "get_employee_groupedby_last_name_orderedby_all",
        component: get_employee_groupedby_last_name_orderedby_all,
        
        },
        
        {
        
        path: "employee/get_employee_filteredby_first_name_middle_name_last_name_groupedby_middle_name",
        name: "get_employee_filteredby_first_name_middle_name_last_name_groupedby_middle_name",
        component: get_employee_filteredby_first_name_middle_name_last_name_groupedby_middle_name,
        
        },
        
        {
        
        path: "employee/get_employee_filteredby_last_name_birth_date_groupedby_employee_supervision_ssn_salary_birth_date",
        name: "get_employee_filteredby_last_name_birth_date_groupedby_employee_supervision_ssn_salary_birth_date",
        component: get_employee_filteredby_last_name_birth_date_groupedby_employee_supervision_ssn_salary_birth_date,
        
        },
        
        {
        
        path: "employee/get_employee_filteredby_last_name_groupedby_birth_date",
        name: "get_employee_filteredby_last_name_groupedby_birth_date",
        component: get_employee_filteredby_last_name_groupedby_birth_date,
        
        },
        
        {
        
        path: "employee/get_employee_filteredby_last_name_groupedby_birth_date_orderedby_employee_supervision_ssn",
        name: "get_employee_filteredby_last_name_groupedby_birth_date_orderedby_employee_supervision_ssn",
        component: get_employee_filteredby_last_name_groupedby_birth_date_orderedby_employee_supervision_ssn,
        
        },
        
        {
        
        path: "employee/get_employee_filteredby_last_name_groupedby_birth_date_orderedby_salary",
        name: "get_employee_filteredby_last_name_groupedby_birth_date_orderedby_salary",
        component: get_employee_filteredby_last_name_groupedby_birth_date_orderedby_salary,
        
        },
        
        {
        
        path: "employee/get_employee_filteredby_last_name_orderedby_employee_supervision_ssn",
        name: "get_employee_filteredby_last_name_orderedby_employee_supervision_ssn",
        component: get_employee_filteredby_last_name_orderedby_employee_supervision_ssn,
        
        },
        
        {
        
        path: "employee/get_employee_filteredby_salary_groupedby_birth_date_salary_employee_supervision_ssn",
        name: "get_employee_filteredby_salary_groupedby_birth_date_salary_employee_supervision_ssn",
        component: get_employee_filteredby_salary_groupedby_birth_date_salary_employee_supervision_ssn,
        
        },
        
        {
        
        path: "employee/get_employee_filteredby_salary_groupedby_birth_date_orderedby_birth_date",
        name: "get_employee_filteredby_salary_groupedby_birth_date_orderedby_birth_date",
        component: get_employee_filteredby_salary_groupedby_birth_date_orderedby_birth_date,
        
        },
        
        {
        
        path: "employee/get_employee_filteredby_salary_groupedby_birth_date_orderedby_employee_supervision_ssn",
        name: "get_employee_filteredby_salary_groupedby_birth_date_orderedby_employee_supervision_ssn",
        component: get_employee_filteredby_salary_groupedby_birth_date_orderedby_employee_supervision_ssn,
        
        },
        
        {
        
        path: "employee/get_employee_filteredby_salary_groupedby_birth_date_orderedby_salary",
        name: "get_employee_filteredby_salary_groupedby_birth_date_orderedby_salary",
        component: get_employee_filteredby_salary_groupedby_birth_date_orderedby_salary,
        
        },
        
        {
        
        path: "employee/get_employee_filteredby_birth_date_groupedby_birth_date",
        name: "get_employee_filteredby_birth_date_groupedby_birth_date",
        component: get_employee_filteredby_birth_date_groupedby_birth_date,
        
        },
        
        {
        
        path: "employee/get_employee_groupedby_birth_date_orderedby_employee_supervision_ssn",
        name: "get_employee_groupedby_birth_date_orderedby_employee_supervision_ssn",
        component: get_employee_groupedby_birth_date_orderedby_employee_supervision_ssn,
        
        },
        
        {
        
        path: "employee/get_employee_filteredby_sex_salary",
        name: "get_employee_filteredby_sex_salary",
        component: get_employee_filteredby_sex_salary,
        
        },
        
        {
        
        path: "employee/get_employee_groupedby_sex_orderedby_sex",
        name: "get_employee_groupedby_sex_orderedby_sex",
        component: get_employee_groupedby_sex_orderedby_sex,
        
        },
        
        {
        
        path: "employee/get_employee_groupedby_sex_orderedby_all",
        name: "get_employee_groupedby_sex_orderedby_all",
        component: get_employee_groupedby_sex_orderedby_all,
        
        },
        
        {
        
        path: "employee/get_employee_groupedby_address_orderedby_all",
        name: "get_employee_groupedby_address_orderedby_all",
        component: get_employee_groupedby_address_orderedby_all,
        
        },
        
        {
        
        path: "employee/get_employee_filteredby_salary_orderedby_employee_supervision_ssn",
        name: "get_employee_filteredby_salary_orderedby_employee_supervision_ssn",
        component: get_employee_filteredby_salary_orderedby_employee_supervision_ssn,
        
        },
        
        {
        
        path: "employee/get_employee_filteredby_salary_orderedby_salary",
        name: "get_employee_filteredby_salary_orderedby_salary",
        component: get_employee_filteredby_salary_orderedby_salary,
        
        },
        
        {
        
        path: "employee/get_employee_groupedby_salary_orderedby_all",
        name: "get_employee_groupedby_salary_orderedby_all",
        component: get_employee_groupedby_salary_orderedby_all,
        
        },
        
        {
        
        path: "employee/get_employee_orderedby_all",
        name: "get_employee_orderedby_all",
        component: get_employee_orderedby_all,
        
        },
        
        {
        
        path: "employee/get_employee_groupedby_employee_supervision_ssn_orderedby_all",
        name: "get_employee_groupedby_employee_supervision_ssn_orderedby_all",
        component: get_employee_groupedby_employee_supervision_ssn_orderedby_all,
        
        },
        
        {
        
        path: "dependent/get_dependent_groupedby_all",
        name: "get_dependent_groupedby_all",
        component: get_dependent_groupedby_all,
        
        },
        
        {
        
        path: "dependent/get_dependent_filteredby_sex",
        name: "get_dependent_filteredby_sex",
        component: get_dependent_filteredby_sex,
        
        },
        
        {
        
        path: "department_location/get_department_location",
        name: "get_department_location",
        component: get_department_location,
        
        },
        
        {
        
        path: "department_location/create_department_location",
        name: "create_department_location",
        component: create_department_location,
        
        },
        
        {
        
        path: "works_employee_project/get_works_employee_project_filteredby_project_name_groupedby_all",
        name: "get_works_employee_project_filteredby_project_name_groupedby_all",
        component: get_works_employee_project_filteredby_project_name_groupedby_all,
        
        },
        
        {
        
        path: "works_employee_project/get_works_employee_project_filteredby_project_name",
        name: "get_works_employee_project_filteredby_project_name",
        component: get_works_employee_project_filteredby_project_name,
        
        },
        
        {
        
        path: "works_employee_project/get_works_employee_project_groupedby_all",
        name: "get_works_employee_project_groupedby_all",
        component: get_works_employee_project_groupedby_all,
        
        },
        
        {
        
        path: "employee_department_location_department/get_employee_department_location_department",
        name: "get_employee_department_location_department",
        component: get_employee_department_location_department,
        
        },
        
        {
        
        path: "employee_department_location_department/get_employee_department_location_department_filteredby_department_name_groupedby_middle_name_address_department_name_last_name",
        name: "get_employee_department_location_department_filteredby_department_name_groupedby_middle_name_address_department_name_last_name",
        component: get_employee_department_location_department_filteredby_department_name_groupedby_middle_name_address_department_name_last_name,
        
        },
        
        {
        
        path: "employee_department_location_department/get_employee_department_location_department_filteredby_department_name_groupedby_middle_name_last_name_department_name",
        name: "get_employee_department_location_department_filteredby_department_name_groupedby_middle_name_last_name_department_name",
        component: get_employee_department_location_department_filteredby_department_name_groupedby_middle_name_last_name_department_name,
        
        },
        
        {
        
        path: "employee_department_location_department/get_employee_department_location_department_groupedby_department_name_orderedby_employee_supervision_ssn",
        name: "get_employee_department_location_department_groupedby_department_name_orderedby_employee_supervision_ssn",
        component: get_employee_department_location_department_groupedby_department_name_orderedby_employee_supervision_ssn,
        
        },
        
    ]
  }
];
        
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
    