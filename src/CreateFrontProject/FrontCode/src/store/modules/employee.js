
import axios from "axios";
const state = {
		get_employee_filteredby_middle_name_last_name_groupedby_all:[],
		get_employee_filteredby_first_name_groupedby_all:[],
		get_employee_filteredby_last_name_groupedby_all_orderedby_salary:[],
		get_employee_filteredby_last_name_groupedby_all:[],
		get_employee_filteredby_last_name_orderedby_salary:[],
		get_employee_filteredby_sex_groupedby_all:[],
		get_employee_orderedby_status:[],
		get_employee_filteredby_salary_groupedby_all:[],
		get_employee_filteredby_middle_name:[],
		get_employee_groupedby_all:[],
		get_employee_groupedby_all_orderedby_birth_date:[],
		get_employee_filteredby_employee_supervision_ssn_groupedby_salary_middle_name_last_name_employee_supervision_ssn:[],
		get_employee_groupedby_salary_middle_name_last_name:[],
		get_employee_groupedby_salary_last_name_orderedby_all:[],
		get_employee_groupedby_middle_name_last_name_orderedby_all:[],
		get_employee_groupedby_last_name_employee_supervision_ssn_orderedby_all:[],
		get_employee_groupedby_last_name_orderedby_all:[],
		get_employee_filteredby_first_name_middle_name_last_name_groupedby_middle_name:[],
		get_employee_filteredby_last_name_birth_date_groupedby_employee_supervision_ssn_salary_birth_date:[],
		get_employee_filteredby_last_name_groupedby_birth_date:[],
		get_employee_filteredby_last_name_groupedby_birth_date_orderedby_employee_supervision_ssn:[],
		get_employee_filteredby_last_name_groupedby_birth_date_orderedby_salary:[],
		get_employee_filteredby_last_name_orderedby_employee_supervision_ssn:[],
		get_employee_filteredby_salary_groupedby_birth_date_salary_employee_supervision_ssn:[],
		get_employee_filteredby_salary_groupedby_birth_date_orderedby_birth_date:[],
		get_employee_filteredby_salary_groupedby_birth_date_orderedby_employee_supervision_ssn:[],
		get_employee_filteredby_salary_groupedby_birth_date_orderedby_salary:[],
		get_employee_filteredby_birth_date_groupedby_birth_date:[],
		get_employee_groupedby_birth_date_orderedby_employee_supervision_ssn:[],
		get_employee_filteredby_sex_salary:[],
		get_employee_groupedby_sex_orderedby_sex:[],
		get_employee_groupedby_sex_orderedby_all:[],
		get_employee_groupedby_address_orderedby_all:[],
		get_employee_filteredby_salary_orderedby_employee_supervision_ssn:[],
		get_employee_filteredby_salary_orderedby_salary:[],
		get_employee_groupedby_salary_orderedby_all:[],
		get_employee_orderedby_all:[],
		get_employee_groupedby_employee_supervision_ssn_orderedby_all:[],

};

const actions = {
		async get_employee_filteredby_middle_name_last_name_groupedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_middle_name_last_name_groupedby_all",
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
            			state.get_employee_filteredby_middle_name_last_name_groupedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_filteredby_first_name_groupedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_first_name_groupedby_all",
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
            			state.get_employee_filteredby_first_name_groupedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_filteredby_last_name_groupedby_all_orderedby_salary({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_last_name_groupedby_all_orderedby_salary",
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
            			state.get_employee_filteredby_last_name_groupedby_all_orderedby_salary = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_filteredby_last_name_groupedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_last_name_groupedby_all",
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
            			state.get_employee_filteredby_last_name_groupedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_filteredby_last_name_orderedby_salary({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_last_name_orderedby_salary",
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
            			state.get_employee_filteredby_last_name_orderedby_salary = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_filteredby_sex_groupedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_sex_groupedby_all",
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
            			state.get_employee_filteredby_sex_groupedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_orderedby_status({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_orderedby_status",
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
            			state.get_employee_orderedby_status = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_filteredby_salary_groupedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_salary_groupedby_all",
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
            			state.get_employee_filteredby_salary_groupedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_filteredby_middle_name({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_middle_name",
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
            			state.get_employee_filteredby_middle_name = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_groupedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_groupedby_all",
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
            			state.get_employee_groupedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_groupedby_all_orderedby_birth_date({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_groupedby_all_orderedby_birth_date",
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
            			state.get_employee_groupedby_all_orderedby_birth_date = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_filteredby_employee_supervision_ssn_groupedby_salary_middle_name_last_name_employee_supervision_ssn({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_employee_supervision_ssn_groupedby_salary_middle_name_last_name_employee_supervision_ssn",
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
            			state.get_employee_filteredby_employee_supervision_ssn_groupedby_salary_middle_name_last_name_employee_supervision_ssn = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_groupedby_salary_middle_name_last_name({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_groupedby_salary_middle_name_last_name",
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
            			state.get_employee_groupedby_salary_middle_name_last_name = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_groupedby_salary_last_name_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_groupedby_salary_last_name_orderedby_all",
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
            			state.get_employee_groupedby_salary_last_name_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_groupedby_middle_name_last_name_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_groupedby_middle_name_last_name_orderedby_all",
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
            			state.get_employee_groupedby_middle_name_last_name_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_groupedby_last_name_employee_supervision_ssn_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_groupedby_last_name_employee_supervision_ssn_orderedby_all",
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
            			state.get_employee_groupedby_last_name_employee_supervision_ssn_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_groupedby_last_name_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_groupedby_last_name_orderedby_all",
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
            			state.get_employee_groupedby_last_name_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_filteredby_first_name_middle_name_last_name_groupedby_middle_name({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_first_name_middle_name_last_name_groupedby_middle_name",
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
            			state.get_employee_filteredby_first_name_middle_name_last_name_groupedby_middle_name = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_filteredby_last_name_birth_date_groupedby_employee_supervision_ssn_salary_birth_date({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_last_name_birth_date_groupedby_employee_supervision_ssn_salary_birth_date",
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
            			state.get_employee_filteredby_last_name_birth_date_groupedby_employee_supervision_ssn_salary_birth_date = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_filteredby_last_name_groupedby_birth_date({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_last_name_groupedby_birth_date",
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
            			state.get_employee_filteredby_last_name_groupedby_birth_date = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_filteredby_last_name_groupedby_birth_date_orderedby_employee_supervision_ssn({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_last_name_groupedby_birth_date_orderedby_employee_supervision_ssn",
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
            			state.get_employee_filteredby_last_name_groupedby_birth_date_orderedby_employee_supervision_ssn = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_filteredby_last_name_groupedby_birth_date_orderedby_salary({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_last_name_groupedby_birth_date_orderedby_salary",
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
            			state.get_employee_filteredby_last_name_groupedby_birth_date_orderedby_salary = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_filteredby_last_name_orderedby_employee_supervision_ssn({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_last_name_orderedby_employee_supervision_ssn",
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
            			state.get_employee_filteredby_last_name_orderedby_employee_supervision_ssn = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_filteredby_salary_groupedby_birth_date_salary_employee_supervision_ssn({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_salary_groupedby_birth_date_salary_employee_supervision_ssn",
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
            			state.get_employee_filteredby_salary_groupedby_birth_date_salary_employee_supervision_ssn = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_filteredby_salary_groupedby_birth_date_orderedby_birth_date({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_salary_groupedby_birth_date_orderedby_birth_date",
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
            			state.get_employee_filteredby_salary_groupedby_birth_date_orderedby_birth_date = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_filteredby_salary_groupedby_birth_date_orderedby_employee_supervision_ssn({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_salary_groupedby_birth_date_orderedby_employee_supervision_ssn",
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
            			state.get_employee_filteredby_salary_groupedby_birth_date_orderedby_employee_supervision_ssn = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_filteredby_salary_groupedby_birth_date_orderedby_salary({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_salary_groupedby_birth_date_orderedby_salary",
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
            			state.get_employee_filteredby_salary_groupedby_birth_date_orderedby_salary = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_filteredby_birth_date_groupedby_birth_date({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_birth_date_groupedby_birth_date",
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
            			state.get_employee_filteredby_birth_date_groupedby_birth_date = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_groupedby_birth_date_orderedby_employee_supervision_ssn({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_groupedby_birth_date_orderedby_employee_supervision_ssn",
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
            			state.get_employee_groupedby_birth_date_orderedby_employee_supervision_ssn = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_filteredby_sex_salary({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_sex_salary",
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
            			state.get_employee_filteredby_sex_salary = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_groupedby_sex_orderedby_sex({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_groupedby_sex_orderedby_sex",
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
            			state.get_employee_groupedby_sex_orderedby_sex = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_groupedby_sex_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_groupedby_sex_orderedby_all",
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
            			state.get_employee_groupedby_sex_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_groupedby_address_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_groupedby_address_orderedby_all",
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
            			state.get_employee_groupedby_address_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_filteredby_salary_orderedby_employee_supervision_ssn({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_salary_orderedby_employee_supervision_ssn",
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
            			state.get_employee_filteredby_salary_orderedby_employee_supervision_ssn = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_filteredby_salary_orderedby_salary({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_filteredby_salary_orderedby_salary",
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
            			state.get_employee_filteredby_salary_orderedby_salary = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_groupedby_salary_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_groupedby_salary_orderedby_all",
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
            			state.get_employee_groupedby_salary_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_orderedby_all",
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
            			state.get_employee_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_employee_groupedby_employee_supervision_ssn_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "employee/get_employee_groupedby_employee_supervision_ssn_orderedby_all",
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
            			state.get_employee_groupedby_employee_supervision_ssn_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},

    };

export default {
  namespaced: true,
  state,
  actions,
};
    