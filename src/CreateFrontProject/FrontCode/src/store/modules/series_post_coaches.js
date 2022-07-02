
import axios from "axios";
const state = {
		get_series_post_coaches:[],

};

const actions = {
		async get_series_post_coaches({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "series_post/coaches/get_series_post_coaches",
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
            			state.get_series_post_coaches = store_data;
		} catch (error) {
			console.log(error)
		}},

    };

export default {
  namespaced: true,
  state,
  actions,
};
    