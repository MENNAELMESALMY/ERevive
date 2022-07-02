
import axios from "axios";
const state = {
		get_awards_players_player_allstar_groupedby_minutes:[],
		get_awards_players_player_allstar_orderedby_minutes:[],

};

const actions = {
		async get_awards_players_player_allstar_groupedby_minutes({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_players/player_allstar/get_awards_players_player_allstar_groupedby_minutes",
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
            			state.get_awards_players_player_allstar_groupedby_minutes = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_players_player_allstar_orderedby_minutes({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_players/player_allstar/get_awards_players_player_allstar_orderedby_minutes",
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
            			state.get_awards_players_player_allstar_orderedby_minutes = store_data;
		} catch (error) {
			console.log(error)
		}},

    };

export default {
  namespaced: true,
  state,
  actions,
};
    