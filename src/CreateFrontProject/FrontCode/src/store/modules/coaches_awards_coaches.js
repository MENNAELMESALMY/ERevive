
import axios from "axios";
const state = {
		get_coaches_awards_coaches_filteredby_year:[],
		get_awards_coaches_coaches_groupedby_coachID:[],
		get_awards_coaches_coaches_orderedby_all:[],

};

const actions = {
		async get_coaches_awards_coaches_filteredby_year({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "coaches/awards_coaches/get_coaches_awards_coaches_filteredby_year",
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
            			state.get_coaches_awards_coaches_filteredby_year = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_coaches_coaches_groupedby_coachID({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_coaches/coaches/get_awards_coaches_coaches_groupedby_coachID",
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
            			state.get_awards_coaches_coaches_groupedby_coachID = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_coaches_coaches_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_coaches/coaches/get_awards_coaches_coaches_orderedby_all",
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
            			state.get_awards_coaches_coaches_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},

    };

export default {
  namespaced: true,
  state,
  actions,
};
    