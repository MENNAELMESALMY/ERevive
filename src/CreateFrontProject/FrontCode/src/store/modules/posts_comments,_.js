
import axios from "axios";
const state = {
		get_posts_comments,__filteredby__incrementalkey_groupedby_all:[],
		get_posts_comments,__groupedby_all:[],
		get_posts_comments,__groupedby_all_orderedby_all:[],
		get_posts_comments,__filteredby__incrementalkey_comments,_incrementalkey_groupedby__incrementalkey:[],
		get_posts_comments,__groupedby__incrementalkey_orderedby_all:[],
		get_posts_comments,__orderedby_all:[],

};

const actions = {
		async get_posts_comments,__filteredby__incrementalkey_groupedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "posts_comments,_/get_posts_comments,__filteredby__incrementalkey_groupedby_all",
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
            			state.get_posts_comments,__filteredby__incrementalkey_groupedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_posts_comments,__groupedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "posts_comments,_/get_posts_comments,__groupedby_all",
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
            			state.get_posts_comments,__groupedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_posts_comments,__groupedby_all_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "posts_comments,_/get_posts_comments,__groupedby_all_orderedby_all",
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
            			state.get_posts_comments,__groupedby_all_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_posts_comments,__filteredby__incrementalkey_comments,_incrementalkey_groupedby__incrementalkey({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "posts_comments,_/get_posts_comments,__filteredby__incrementalkey_comments,_incrementalkey_groupedby__incrementalkey",
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
            			state.get_posts_comments,__filteredby__incrementalkey_comments,_incrementalkey_groupedby__incrementalkey = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_posts_comments,__groupedby__incrementalkey_orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "posts_comments,_/get_posts_comments,__groupedby__incrementalkey_orderedby_all",
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
            			state.get_posts_comments,__groupedby__incrementalkey_orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},
		async get_posts_comments,__orderedby_all({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "posts_comments,_/get_posts_comments,__orderedby_all",
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
            			state.get_posts_comments,__orderedby_all = store_data;
		} catch (error) {
			console.log(error)
		}},

    };

export default {
  namespaced: true,
  state,
  actions,
};
    