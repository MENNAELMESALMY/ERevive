import axios from "axios";
import router from "../../router/index";

const state = {
  predictedClusters: {},
  deletedQuery: "",
  deletedQueryName: "",
  clusters: [],
  currentClusterName: "",
  queries: [],
  formData: {},
  appFinished: false,
  systemName: "",
  systemDescription: "",
  databaseName: "",
  databaseUsername: "",
  databasePassword: "",
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
  setAppFinished(state, finished) {
    state.appFinished = finished;
  },
  setSystemInfo(state, systemObject) {
    state.systemName = systemObject.systemName;
    state.systemDescription = systemObject.systemDescription;
    state.databaseName = systemObject.databaseName;
    state.databaseUsername = systemObject.databaseUsername;
    state.datbasePassword = systemObject.databasePassword;
  },
};

const actions = {
  postSearchEngineQueries({ commit, state }, payload) {
    let schema = {
      schema: payload.finalSchema,
    };
    state.formData = payload.formData;
    axios
      .post("/searchengine", schema)
      .then((response) => {
        console.log("search Engine Output", response.data);
        commit("setSearchEngineQueries", response.data);
        router.push("/clustersPage");
      })
      .catch((error) => {
        console.log(error);
      });
  },
  postStartApplication({ commit, state }) {
    let systemData = {
      forms: state.formData,
      systemData: {
        systemName: state.systemName,
        systemDescription: state.systemDescription,
        databaseName: state.databaseName,
        databaseUsername: state.databaseUsername,
        databasePassword: state.databasePassword,
      },
    };
    axios
      .post("/application", systemData)
      .then(() => {
        commit("setAppFinished", true);
        router.push("/lastPage");
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
