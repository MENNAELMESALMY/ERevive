
import axios from "axios";
const state = {
		get_awards_coaches:[],
		get_awards_coaches_filteredby_coachID_id:[],

};

const actions = {
		async get_awards_coaches({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_coaches/get_awards_coaches",
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
            			state.get_awards_coaches = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_coaches_filteredby_coachID_id({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_coaches/get_awards_coaches_filteredby_coachID_id",
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
            			state.get_awards_coaches_filteredby_coachID_id = store_data;
		} catch (error) {
			console.log(error)
		}},

    };

export default {
  namespaced: true,
  state,
  actions,
};
    