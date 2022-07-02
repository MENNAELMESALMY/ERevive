
import axios from "axios";
const state = {
		get_awards_players_teams_filteredby_name_groupedby_name:[],
		get_awards_players_teams_groupedby_playerID:[],
		get_awards_players_teams:[],
		get_awards_players_teams_filteredby_name_year:[],
		get_awards_players_teams_filteredby_year:[],

};

const actions = {
		async get_awards_players_teams_filteredby_name_groupedby_name({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_players/teams/get_awards_players_teams_filteredby_name_groupedby_name",
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
            			state.get_awards_players_teams_filteredby_name_groupedby_name = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_players_teams_groupedby_playerID({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_players/teams/get_awards_players_teams_groupedby_playerID",
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
            			state.get_awards_players_teams_groupedby_playerID = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_players_teams({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_players/teams/get_awards_players_teams",
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
            			state.get_awards_players_teams = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_players_teams_filteredby_name_year({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_players/teams/get_awards_players_teams_filteredby_name_year",
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
            			state.get_awards_players_teams_filteredby_name_year = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_players_teams_filteredby_year({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_players/teams/get_awards_players_teams_filteredby_year",
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
            			state.get_awards_players_teams_filteredby_year = store_data;
		} catch (error) {
			console.log(error)
		}},

    };

export default {
  namespaced: true,
  state,
  actions,
};
    