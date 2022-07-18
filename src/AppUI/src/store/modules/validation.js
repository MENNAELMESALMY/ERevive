import axios from "axios";
const state = {
  formData: {},
};
const actions = {
  async sendSchema({ state }, payload) {
    let schema = { schema: payload.finalSchema };
    state.formData = payload.formData;
    try {
      await axios.post("/searchengine", schema);
    } catch (err) {
      console.log(err);
      router.push("/errorPage");
    }
  },
};
export default {
  namespaced: true,
  state,
  actions,
};
