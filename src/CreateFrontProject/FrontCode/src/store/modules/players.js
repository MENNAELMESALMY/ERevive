
import axios from "axios";
const state = {
		get_players_filteredby_playerID_groupedby_all:[],
		get_players_filteredby_height_groupedby_all:[],
		get_players_filteredby_weight_groupedby_all:[],
		get_players_groupedby_all:[],

};

const actions = {
		async get_players_filteredby_playerID_groupedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "players/get_players_filteredby_playerID_groupedby_all",
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
            			state.get_players_filteredby_playerID_groupedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_players_filteredby_height_groupedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "players/get_players_filteredby_height_groupedby_all",
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
            			state.get_players_filteredby_height_groupedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_players_filteredby_weight_groupedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "players/get_players_filteredby_weight_groupedby_all",
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
            			state.get_players_filteredby_weight_groupedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_players_groupedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "players/get_players_groupedby_all",
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
            			state.get_players_groupedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},

    };

export default {
  namespaced: true,
  state,
  actions,
};
    