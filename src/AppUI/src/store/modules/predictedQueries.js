import axios from "axios";
import router from "../../router/index";

const state = {
  predictedClusters: {},
  deletedQuery: "",
  deletedQueryName: "",
  clusters: [],
  currentClusterName: "",
  queries: [],
};

const mutations = {
  setQueries(state, queriesList) {
    state.queries = queriesList;
  },
  setDeletedQuery(state, queryObject) {
    state.deletedQuery = queryObject.query;
    state.deletedQueryName = queryObject.queryName;
  },
  deleteQuery(state, queryObject) {
    state.queries = state.queries.filter(
      (item) =>
        item.name !== queryObject.queryName && item.query !== queryObject.query
    );
  },
  editQuery(state, queryObject) {
    state.queries.map((item) => {
      if (
        item.name == queryObject.oldQueryName &&
        item.query == queryObject.oldQuery
      ) {
        item.query = queryObject.query;
        item.name = queryObject.queryName;
      }
    });
  },
  addNewQuery(state, queryObject) {
    state.queries.push({
      name: queryObject.queryName,
      query: queryObject.query,
    });
  },
  setCurrentCluster(state, clusterName) {
    state.currentClusterName = clusterName;
    state.queries = state.predictedClusters[clusterName];
  },
  setSearchEngineQueries(state, clusters) {
    state.clusters = Object.keys(clusters);
    state.predictedClusters = clusters;
  },
};

const actions = {
  getSearchEngineQueries({ commit }) {
    axios
      .get("/seoutput")
      .then((response) => {
        console.log("seoutput", response.data);
        commit("setSearchEngineQueries", response.data);
        router.push("/clustersPage");
      })
      .catch((error) => {
        console.log(error);
      });
  },
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
};
