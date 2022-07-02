
import axios from "axios";
const state = {
		get_awards_coaches_coaches_players:[],
		get_awards_coaches_coaches_players_filteredby_year:[],
		get_awards_coaches_coaches_players_filteredby_playerID:[],

};

const actions = {
		async get_awards_coaches_coaches_players({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_coaches/coaches/players/get_awards_coaches_coaches_players",
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
            			state.get_awards_coaches_coaches_players = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_coaches_coaches_players_filteredby_year({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_coaches/coaches/players/get_awards_coaches_coaches_players_filteredby_year",
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
            			state.get_awards_coaches_coaches_players_filteredby_year = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_coaches_coaches_players_filteredby_playerID({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_coaches/coaches/players/get_awards_coaches_coaches_players_filteredby_playerID",
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
            			state.get_awards_coaches_coaches_players_filteredby_playerID = store_data;
		} catch (error) {
			console.log(error)
		}},

    };

export default {
  namespaced: true,
  state,
  actions,
};
    