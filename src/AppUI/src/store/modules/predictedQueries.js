import axios from "axios";
import router from "../../router/index";

const state = {
  predictedClusters: {},
  deletedQuery: "",
  deletedQueryName: "",
  clusters: [],
  currentClusterName: "",
  formData: {},
  appFinished: false,
  systemName: "",
  systemDescription: "",
  databaseName: "",
  databaseUsername: "",
  databasePassword: "",
  testSchema: {},
  schemaGraph: {},
  entityDict: {},
  schemaEntityNames: {},
  loadingTitle: "Image Processing is Running ....",
  queriesErrors: {},
  errorsClusters: [],
};

const mutations = {
  setQueries(state, queriesList) {
    state.queries = queriesList;
  },
  setLoadingTitle(state, title) {
    state.loadingTitle = title;
  },
  setDeletedQuery(state, queryObject) {
    state.deletedQuery = queryObject.query;
    state.deletedQueryName = queryObject.queryName;
  },
  deleteQuery(state, queryObject) {
    let queries = state.predictedClusters[state.currentClusterName];
    queries.filter(
      (item) =>
        item.ui_name !== queryObject.queryName &&
        item.query[0] !== queryObject.query
    );
  },
  editQuery(state, queryObject) {
    let queries = state.predictedClusters[state.currentClusterName];
    queries.map((item) => {
      if (
        item.ui_name == queryObject.oldQueryName &&
        item.query[0] == queryObject.oldQuery
      ) {
        item.query[0] = queryObject.query;
        item.ui_name = queryObject.queryName;
        item.is_updated = true;
      }
    });
  },
  addNewQuery(state, queryObject) {
    let queries = state.predictedClusters[state.currentClusterName];
    let copiedObject = queries[0];
    let newObject = {
      ui_name: queryObject.queryName,
      query: [queryObject.query],
      is_updated: false,
      ...copiedObject,
    };
    queries.push(newObject);
  },
  setCurrentCluster(state, clusterName) {
    state.currentClusterName = clusterName;
  },
  setSearchEngineQueries(state, clusters) {
    state.testSchema = clusters.searchOut.testSchema;
    state.schemaGraph = clusters.searchOut.schemaGraph;
    state.entityDict = clusters.searchOut.entityDict;
    state.schemaEntityNames = clusters.searchOut.schemaEntityNames;
    state.clusters = Object.keys(clusters.searchOut.clusters);
    state.predictedClusters = clusters.searchOut.clusters;
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
  setQueriesErrors(state, errors) {
    state.queriesErrors = errors;
    state.errorsClusters = Object.keys(errors);
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
  postValidate({ commit, state }) {
    let updatedClusters = {
      testSchema: state.testSchema,
      schemaGraph: state.schemaGraph,
      entityDict: state.entityDict,
      schemaEntityNames: state.schemaEntityNames,
      clusters: state.predictedClusters,
    };
    axios
      .post("/validate", updatedClusters)
      .then((response) => {
        if (response.status == 200) {
          commit("setLoadingTitle", "Creating Application ...");
          router.push("/loadingPage");
          this.postStartApplication();
        }
      })
      .catch((error) => {
        console.log(error);
        commit("setQueriesErrors", error.response.data);
        router.push("/queriesErrors");
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
      clusters: state.predictedClusters,
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
