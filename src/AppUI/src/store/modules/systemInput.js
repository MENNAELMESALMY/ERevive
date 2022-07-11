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
  setIpOutputData(state, ipOutputData) {
    state.numEntities = ipOutputData.detectedShapes.rectangle.totalCount;
    state.numRelations = ipOutputData.detectedShapes.diamond.totalCount;
    state.numAttributes = ipOutputData.detectedShapes.oval.totalCount;
    state.stringPercent = ipOutputData.dataTypes.str;
    state.intPercent = ipOutputData.dataTypes.int;
    state.floatPercent = ipOutputData.dataTypes.float;
    state.datePercent = ipOutputData.dataTypes.datetime;
    state.booleanPercent = ipOutputData.dataTypes.bool;
    state.numPrimaryKeys = ipOutputData.detectedKeys;
    state.numMultivalued =
      ipOutputData.detectedShapes.oval.multivaluedAttrCount;
    state.numIdentifying =
      ipOutputData.detectedShapes.diamond.IdentifyingRelationCount;
    state.numWeakEntities = ipOutputData.detectedShapes.rectangle.weakCount;
    state.naryNum = ipOutputData.detectedRelations.naryRelation;
    state.fullNum = ipOutputData.detectedRelations.fullParticipation;
    state.partialNum = ipOutputData.detectedRelations.partialParticipation;
    state.numOneToOne = ipOutputData.detectedRelations.oneToOne;
    state.numOneToMany = ipOutputData.detectedRelations.oneToMany;
    state.numManyToMany = ipOutputData.detectedRelations.manyToMany;
    state.totalTime = ipOutputData.totalTime;
  },
};

const actions = {
  async postImage({ commit }, payload) {
    try {
      await axios.post("/imageprocessing", payload.image);
      commit("setErImage", payload.image);
    } catch (err) {
      console.log(err);
    }
  },
  getIpOutput({ commit, state }) {
    axios
      .get("/ipoutput")
      .then((response) => {
        state.ipOutPutReturned = true;
        commit("setIpOutputData", response.data);
        router.push("/ipOutput");
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
