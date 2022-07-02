
import axios from "axios";
const state = {
		get_works_employee_project_filteredby_project_name_groupedby_all:[],
		get_works_employee_project_filteredby_project_name:[],
		get_works_employee_project_groupedby_all:[],

};

const actions = {
		async get_works_employee_project_filteredby_project_name_groupedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "works_employee_project/get_works_employee_project_filteredby_project_name_groupedby_all",
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
            			state.get_works_employee_project_filteredby_project_name_groupedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_works_employee_project_filteredby_project_name({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "works_employee_project/get_works_employee_project_filteredby_project_name",
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
            			state.get_works_employee_project_filteredby_project_name = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_works_employee_project_groupedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "works_employee_project/get_works_employee_project_groupedby_all",
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
            			state.get_works_employee_project_groupedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},

    };

export default {
  namespaced: true,
  state,
  actions,
};
    