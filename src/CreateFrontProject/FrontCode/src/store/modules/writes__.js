
import axios from "axios";
const state = {
		get_writes__:[],
		create_writes__:[],

};

const actions = {
		async get_writes__({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "/writes__",
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
            			state.get_writes__ = store_data;
		} catch (error) {
			console.log(error)
		}},
		async create_writes__({ state }, payload) {
		try{
			const response = await axios({
			method: "post",
			url: "/writes__",
			data: payload.body_param,})
		} catch (error) {
			console.log(error)
		}},

    };

export default {
  namespaced: true,
  state,
  actions,
};
    