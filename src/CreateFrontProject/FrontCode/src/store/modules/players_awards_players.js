
import axios from "axios";
const state = {
		get_players_awards_players_filteredby_playerID_groupedby_all:[],
		get_awards_players_players_groupedby_birthCity_playerID_firstName_birthCountry_middleName_orderedby_all:[],
		get_players_awards_players_groupedby_all:[],
		get_awards_players_players_filteredby_year:[],
		get_players_awards_players_groupedby_playerID:[],
		get_players_awards_players_groupedby_playerID_lgID_orderedby_all:[],
		get_awards_players_players_filteredby_firstName_middleName_groupedby_playerID:[],
		get_players_awards_players_groupedby_hsCity_playerID_year_orderedby_all:[],
		get_awards_players_players_filteredby_height:[],

};

const actions = {
		async get_players_awards_players_filteredby_playerID_groupedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "players/awards_players/get_players_awards_players_filteredby_playerID_groupedby_all",
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
            			state.get_players_awards_players_filteredby_playerID_groupedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_players_players_groupedby_birthCity_playerID_firstName_birthCountry_middleName_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_players/players/get_awards_players_players_groupedby_birthCity_playerID_firstName_birthCountry_middleName_orderedby_all",
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
            			state.get_awards_players_players_groupedby_birthCity_playerID_firstName_birthCountry_middleName_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_players_awards_players_groupedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "players/awards_players/get_players_awards_players_groupedby_all",
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
            			state.get_players_awards_players_groupedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_players_players_filteredby_year({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_players/players/get_awards_players_players_filteredby_year",
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
            			state.get_awards_players_players_filteredby_year = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_players_awards_players_groupedby_playerID({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "players/awards_players/get_players_awards_players_groupedby_playerID",
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
            			state.get_players_awards_players_groupedby_playerID = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_players_awards_players_groupedby_playerID_lgID_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "players/awards_players/get_players_awards_players_groupedby_playerID_lgID_orderedby_all",
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
            			state.get_players_awards_players_groupedby_playerID_lgID_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_players_players_filteredby_firstName_middleName_groupedby_playerID({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_players/players/get_awards_players_players_filteredby_firstName_middleName_groupedby_playerID",
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
            			state.get_awards_players_players_filteredby_firstName_middleName_groupedby_playerID = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_players_awards_players_groupedby_hsCity_playerID_year_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "players/awards_players/get_players_awards_players_groupedby_hsCity_playerID_year_orderedby_all",
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
            			state.get_players_awards_players_groupedby_hsCity_playerID_year_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_players_players_filteredby_height({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_players/players/get_awards_players_players_filteredby_height",
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
            			state.get_awards_players_players_filteredby_height = store_data;
		} catch (error) {
			console.log(error)
		}},

    };

export default {
  namespaced: true,
  state,
  actions,
};
    