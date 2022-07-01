
import axios from "axios";
const state = {
		get_awards_coaches_series_post_groupedby_all_orderedby_all:[],
		get_awards_coaches_series_post:[],
		get_awards_coaches_series_post_groupedby_coachID_id_orderedby_all:[],
		get_awards_coaches_series_post_groupedby_id:[],
		get_awards_coaches_series_post_groupedby_id_orderedby_all:[],

};

const actions = {
		async get_awards_coaches_series_post_groupedby_all_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_coaches/series_post/get_awards_coaches_series_post_groupedby_all_orderedby_all",
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
            			state.get_awards_coaches_series_post_groupedby_all_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_coaches_series_post({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_coaches/series_post/get_awards_coaches_series_post",
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
            			state.get_awards_coaches_series_post = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_coaches_series_post_groupedby_coachID_id_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_coaches/series_post/get_awards_coaches_series_post_groupedby_coachID_id_orderedby_all",
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
            			state.get_awards_coaches_series_post_groupedby_coachID_id_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_coaches_series_post_groupedby_id({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_coaches/series_post/get_awards_coaches_series_post_groupedby_id",
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
            			state.get_awards_coaches_series_post_groupedby_id = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_awards_coaches_series_post_groupedby_id_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "awards_coaches/series_post/get_awards_coaches_series_post_groupedby_id_orderedby_all",
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
            			state.get_awards_coaches_series_post_groupedby_id_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},

    };

export default {
  namespaced: true,
  state,
  actions,
};
    