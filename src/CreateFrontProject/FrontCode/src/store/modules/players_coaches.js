
import axios from "axios";
const state = {
		get_players_coaches_groupedby_playerID:[],
		get_players_coaches_groupedby_coachID_playerID_orderedby_all:[],
		get_players_coaches:[],
		get_players_coaches_groupedby_playerID_orderedby_all:[],

};

const actions = {
		async get_players_coaches_groupedby_playerID({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "players/coaches/get_players_coaches_groupedby_playerID",
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
            			state.get_players_coaches_groupedby_playerID = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_players_coaches_groupedby_coachID_playerID_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "players/coaches/get_players_coaches_groupedby_coachID_playerID_orderedby_all",
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
            			state.get_players_coaches_groupedby_coachID_playerID_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_players_coaches({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "players/coaches/get_players_coaches",
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
            			state.get_players_coaches = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_players_coaches_groupedby_playerID_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "players/coaches/get_players_coaches_groupedby_playerID_orderedby_all",
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
            			state.get_players_coaches_groupedby_playerID_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},

    };

export default {
  namespaced: true,
  state,
  actions,
};
    