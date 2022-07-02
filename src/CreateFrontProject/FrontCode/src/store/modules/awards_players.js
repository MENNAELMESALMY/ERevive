
import axios from "axios";
const state = {
		get_awards_players_filteredby_year_groupedby_all:[],
		get_awards_players_groupedby_all:[],
		get_awards_players_groupedby_playerID_lgID:[],
		get_awards_players_filteredby_lgID_year_groupedby_year:[],
		get_awards_players_groupedby_playerID_orderedby_all:[],
		get_awards_players_orderedby_all:[],

};

const actions = {
		async get_awards_players_filteredby_year_groupedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_players/get_awards_players_filteredby_year_groupedby_all",
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
            			state.get_awards_players_filteredby_year_groupedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_players_groupedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_players/get_awards_players_groupedby_all",
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
            			state.get_awards_players_groupedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_players_groupedby_playerID_lgID({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_players/get_awards_players_groupedby_playerID_lgID",
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
            			state.get_awards_players_groupedby_playerID_lgID = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_players_filteredby_lgID_year_groupedby_year({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_players/get_awards_players_filteredby_lgID_year_groupedby_year",
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
            			state.get_awards_players_filteredby_lgID_year_groupedby_year = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_players_groupedby_playerID_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_players/get_awards_players_groupedby_playerID_orderedby_all",
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
            			state.get_awards_players_groupedby_playerID_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_players_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_players/get_awards_players_orderedby_all",
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
            			state.get_awards_players_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},

    };

export default {
  namespaced: true,
  state,
  actions,
};
    