import axios from "axios";
import router from "../../router/index";

const state = {
  systemName: "",
  systemDescription: "",
  dataBaseName: "",
  dataBaseUserName: "",
  dataBasePassword: "",
  ipOutPutReturned: false,
  numEntities: 0,
  numRelations: 0,
  numAttributes: 0,
  stringPercent: 0,
  intPercent: 0,
  floatPercent: 0,
  datePercent: 0,
  booleanPercent: 0,
  numPrimaryKeys: 0,
  numMultivalued: 0,
  numIdentifying: 0,
  numWeakEntities: 0,
  naryNum: 0,
  fullNum: 0,
  partialNum: 0,
  numOneToOne: 0,
  numOneToMany: 0,
  numManyToMany: 0,
  totalTime: 0,
  initialSchema: {},
  loadingTitle: "Image Processing is Running ....",
};

const mutations = {
  setSystemInfo(state, systemObject) {
    state.systemName = systemObject.systemName;
    state.systemDescription = systemObject.systemDescription;
    state.dataBaseName = systemObject.dataBaseName;
    state.dataBaseUserName = systemObject.dataBaseUserName;
    state.dataBasePassword = systemObject.dataBasePassword;
  },
  setErImage(state, image) {
    state.erImage = image;
  },
  setLoadingTitle(state, title) {
    state.loadingTitle = title;
  },
  setIpOutputData(state, ipOutputData) {
    state.initialSchema = ipOutputData[0];
    let statistics = ipOutputData[1];
    state.numEntities = statistics.detectedShapes.rectangle.totalCount;
    state.numRelations = statistics.detectedShapes.diamond.totalCount;
    state.numAttributes = statistics.detectedShapes.oval.totalCount;
    state.stringPercent = statistics.dataTypes.str;
    state.intPercent = statistics.dataTypes.int;
    state.floatPercent = statistics.dataTypes.float;
    state.datePercent = statistics.dataTypes.datetime;
    state.booleanPercent = statistics.dataTypes.bool;
    state.numPrimaryKeys = statistics.detectedKeys;
    state.numMultivalued = statistics.detectedShapes.oval.multivaluedAttrCount;
    state.numIdentifying =
      statistics.detectedShapes.diamond.IdentifyingRelationCount;
    state.numWeakEntities = statistics.detectedShapes.rectangle.weakCount;
    state.naryNum = statistics.detectedRelations.naryRelation;
    state.fullNum = statistics.detectedRelations.fullParticipation;
    state.partialNum = statistics.detectedRelations.partialParticipation;
    state.numOneToOne = statistics.detectedRelations.oneToOne;
    state.numOneToMany = statistics.detectedRelations.oneToMany;
    state.numManyToMany = statistics.detectedRelations.manyToMany;
    state.totalTime = statistics.totalTime;
  },
};

const actions = {
  async postImage({ commit }, payload) {
    try {
      await axios.post("/imageprocessing", payload, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      commit("setErImage", payload);
    } catch (err) {
      console.log(err);
    }
  },
  getIpOutput({ commit, state }) {
    if (!state.ipOutPutReturned) {
      axios
        .get("/ipoutput")
        .then((response) => {
          console.log("ipoutput", response.data);
          state.ipOutPutReturned = true;
          commit("setIpOutputData", response.data);
          router.push("/ipOutput");
        })
        .catch((error) => {
          console.log(error);
        });
    }
  },
};
export default {
  namespaced: true,
  state,
  mutations,
  actions,
};
