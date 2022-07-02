
import axios from "axios";
const state = {
		get_employee_department_location_department:[],
		get_employee_department_location_department_filteredby_department_name_groupedby_middle_name_address_department_name_last_name:[],
		get_employee_department_location_department_filteredby_department_name_groupedby_middle_name_last_name_department_name:[],
		get_employee_department_location_department_groupedby_department_name_orderedby_employee_supervision_ssn:[],

};

const actions = {
		async get_employee_department_location_department({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/department_location/department/get_employee_department_location_department",
			params: payload,})

            let results = response.data
            let store_data = []
            for (let i = 0; i < results.length; i++) {
                let item = results[i]
                let store_item = {}
                for (let key in item) {
                    store_item[key.replace('.','_').replace(' ','_')] = item[key]
                }
                store_data.push(store_item)
            }
            			state.get_employee_department_location_department = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_department_location_department_filteredby_department_name_groupedby_middle_name_address_department_name_last_name({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/department_location/department/get_employee_department_location_department_filteredby_department_name_groupedby_middle_name_address_department_name_last_name",
			params: payload,})

            let results = response.data
            let store_data = []
            for (let i = 0; i < results.length; i++) {
                let item = results[i]
                let store_item = {}
                for (let key in item) {
                    store_item[key.replace('.','_').replace(' ','_')] = item[key]
                }
                store_data.push(store_item)
            }
            			state.get_employee_department_location_department_filteredby_department_name_groupedby_middle_name_address_department_name_last_name = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_department_location_department_filteredby_department_name_groupedby_middle_name_last_name_department_name({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/department_location/department/get_employee_department_location_department_filteredby_department_name_groupedby_middle_name_last_name_department_name",
			params: payload,})

            let results = response.data
            let store_data = []
            for (let i = 0; i < results.length; i++) {
                let item = results[i]
                let store_item = {}
                for (let key in item) {
                    store_item[key.replace('.','_').replace(' ','_')] = item[key]
                }
                store_data.push(store_item)
            }
            			state.get_employee_department_location_department_filteredby_department_name_groupedby_middle_name_last_name_department_name = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_department_location_department_groupedby_department_name_orderedby_employee_supervision_ssn({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/department_location/department/get_employee_department_location_department_groupedby_department_name_orderedby_employee_supervision_ssn",
			params: payload,})

            let results = response.data
            let store_data = []
            for (let i = 0; i < results.length; i++) {
                let item = results[i]
                let store_item = {}
                for (let key in item) {
                    store_item[key.replace('.','_').replace(' ','_')] = item[key]
                }
                store_data.push(store_item)
            }
            			state.get_employee_department_location_department_groupedby_department_name_orderedby_employee_supervision_ssn = store_data;
		} catch (error) {
			console.log(error)
		}},

    };

export default {
  namespaced: true,
  state,
  actions,
};
    