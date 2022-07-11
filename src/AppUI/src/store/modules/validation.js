import axios from "axios";
const state = {
  schema: {},
};
const actions = {
  async getSchema({ state }) {
    try {
      let response = await axios.get("/imageprocessing");
      state.schema = response.data;
      console.log(state.schema);
    } catch (err) {
      console.log(err);
    }
  },
  async sendSchema({ state }, payload) {
    try {
      await axios.post("/imageprocessing", payload);
      console.log(state.schema);
    } catch (err) {
      console.log(err);
    }
  },
};
export default {
  namespaced: true,
  state,
  actions,
};
