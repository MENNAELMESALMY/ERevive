
import axios from "axios";
import router from "@/router";
const state = {
		endpoint_name5:[],
		endpoint_name6:[],

};

const actions = {
		async endpoint_name5({ state }, payload) {
		try{
			const response = await axios({
			method: "post",
			url: "",
			data: payload.body_param,})
		} catch (error) {
			console.log(error)
		}},
		async endpoint_name6({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "",
			params: payload.query_param,})
			state.endpoint_name6 = response.data;
		} catch (error) {
			console.log(error)
		}},

    };

export default {
  namespaced: true,
  state,
  actions,
};
    