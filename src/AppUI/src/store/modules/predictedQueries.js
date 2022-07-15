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
  setSeeds: false,
  generatedSql: "",
  finalSchema: {},
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
    state.predictedClusters[state.currentClusterName] = queries.filter(
      (item) =>
        item[0].ui_name !== queryObject.queryName &&
        item[0].query !== queryObject.query
    );

    console.log(
      "state.predictedClusters[state.currentClusterName]",
      state.predictedClusters[state.currentClusterName]
    );
  },
  editQuery(state, queryObject) {
    let queries = state.predictedClusters[state.currentClusterName];
    queries.map((item) => {
      if (
        item[0].ui_name == queryObject.oldQueryName &&
        item[0].query == queryObject.oldQuery
      ) {
        item[0].query = queryObject.query;
        item[0].ui_name = queryObject.queryName;
        item[0].is_updated = true;
      }
    });
  },
  addNewQuery(state, queryObject) {
    let newObject = {
      ui_name: queryObject.queryName,
      query: queryObject.query,
      is_updated: true,
    };
    state.predictedClusters[state.currentClusterName].push([newObject, {}]);
  },
  setCurrentCluster(state, clusterName) {
    state.currentClusterName = clusterName;
  },
  setSearchEngineQueries(state, clusters) {
    state.testSchema = clusters.testSchema;
    state.schemaGraph = clusters.schemaGraph;
    state.entityDict = clusters.entityDict;
    state.schemaEntityNames = clusters.schemaEntityNames;
    state.clusters = Object.keys(clusters.clusters);
    state.predictedClusters = clusters.clusters;
  },
  setAppFinished(state, finished) {
    state.appFinished = finished;
  },
  setSystemInfo(state, systemObject) {
    state.systemName = systemObject.systemName;
    state.systemDescription = systemObject.systemDescription;
    state.databaseName = systemObject.databaseName;
    state.databaseUsername = systemObject.databaseUsername;
    state.databasePassword = systemObject.databasePassword;
    console.log(state);
  },
  setQueriesErrors(state, errors) {
    state.queriesErrors = errors;
    state.errorsClusters = Object.keys(errors);
  },
};

const actions = {
  async postSearchEngineQueries({ commit, state }, payload) {
    let schema = { schema: payload.finalSchema };
    state.finalSchema = payload.finalSchema;
    console.log("sending schema", schema);
    state.formData = payload.formData;
    try {
      let response = await axios({
        method: "post",
        url: "/searchengine",
        headers: {},
        data: schema,
      });
      commit("setSearchEngineQueries", response.data);
      router.push("/clustersPage");
    } catch (error) {
      console.log(error);
    }
  },
  postStartApplication({ commit, state }) {
    console.log("systemName", state.systemName);
    console.log("systemDescription", state.systemDescription);
    console.log("databaseName", state.databaseName);
    console.log("databaseUsername", state.databaseUsername);
    console.log("databasePassword", state.databasePassword);
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
      testSchema: state.testSchema,
    };
    console.log("systemData", systemData);
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
          this.dispatch("predictedQueries/postStartApplication");
        }
      })
      .catch((error) => {
        console.log(error);
        commit("setQueriesErrors", error.response.data);
        router.push("/queriesErrors");
      });
  },
  postAddSeeds({ state }) {
    axios
      .post("/seeds")
      .then(() => {
        state.setSeeds = true;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  postConvertNlpToSql({ state }, payload) {
    let sqlObject = {
      finalSchema: state.finalSchema,
      query: payload.nlpQuestion,
    };
    console.log("sqlObject", sqlObject);
    axios
      .post("/nlptosql", sqlObject)
      .then((response) => {
        state.generatedSql = response.data.query;
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
