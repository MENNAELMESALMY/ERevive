
import axios from "axios";
const state = {
		get_dependent_groupedby_all:[],
		get_dependent_filteredby_sex:[],

};

const actions = {
		async get_dependent_groupedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "dependent/get_dependent_groupedby_all",
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
            			state.get_dependent_groupedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_dependent_filteredby_sex({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "dependent/get_dependent_filteredby_sex",
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
            			state.get_dependent_filteredby_sex = store_data;
		} catch (error) {
			console.log(error)
		}},

    };

export default {
  namespaced: true,
  state,
  actions,
};
    