
import axios from "axios";
const state = {
		get_players_awards_coaches_groupedby_id_firstName_middleName_orderedby_all:[],
		get_players_awards_coaches:[],
		get_players_awards_coaches_filteredby_id:[],
		get_players_awards_coaches_groupedby_id_firstName_middleName:[],

};

const actions = {
		async get_players_awards_coaches_groupedby_id_firstName_middleName_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "players/awards_coaches/get_players_awards_coaches_groupedby_id_firstName_middleName_orderedby_all",
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
            			state.get_players_awards_coaches_groupedby_id_firstName_middleName_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_players_awards_coaches({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "players/awards_coaches/get_players_awards_coaches",
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
            			state.get_players_awards_coaches = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_players_awards_coaches_filteredby_id({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "players/awards_coaches/get_players_awards_coaches_filteredby_id",
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
            			state.get_players_awards_coaches_filteredby_id = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_players_awards_coaches_groupedby_id_firstName_middleName({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "players/awards_coaches/get_players_awards_coaches_groupedby_id_firstName_middleName",
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
            			state.get_players_awards_coaches_groupedby_id_firstName_middleName = store_data;
		} catch (error) {
			console.log(error)
		}},

    };

export default {
  namespaced: true,
  state,
  actions,
};
    