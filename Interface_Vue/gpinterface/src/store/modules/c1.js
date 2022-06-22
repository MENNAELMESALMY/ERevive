
import axios from "axios";
import router from "@/router";
const state = {
		endpoint_name1:[],
		endpoint_name2:[],
		endpoint_name3:[],
		endpoint_name4:[],

};

const actions = {
		async endpoint_name1({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "",
			params: payload.query_param,})
			state.endpoint_name1 = response.data;
		} catch (error) {
			console.log(error)
		}},
		async endpoint_name2({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "",
			params: payload.query_param,})
			state.endpoint_name2 = response.data;
		} catch (error) {
			console.log(error)
		}},
		async endpoint_name3({ state }, payload) {
		try{
			const response = await axios({
			method: "post",
			url: "",
			data: payload.body_param,})
		} catch (error) {
			console.log(error)
		}},
		async endpoint_name4({ state }, payload) {
		try{
			const response = await axios({
			method: "get",
			url: "",
			params: payload.query_param,})
			state.endpoint_name4 = response.data;
		} catch (error) {
			console.log(error)
		}},

    };

export default {
  namespaced: true,
  state,
  actions,
};
    