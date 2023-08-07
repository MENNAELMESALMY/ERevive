import axios from "axios";
import router from "../../router/index";

const state = {
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
  initialSchema: {
    11: {
      TableName: "DEPARTMENT",
      attributes: {
        name: "str",
        start_date: "datetime",
        EMPLOYEE_Manages_attr_1: "str",
      },
      primaryKey: ["name"],
      ForgeinKey: [
        {
          attributeName: "EMPLOYEE_Manages_attr_1",
          ForignKeyTable: "EMPLOYEE",
          ForignKeyTableAttributeName: "attr_1",
          patricipaction: "partial",
          dataType: "str",
        },
      ],
      isWeak: false,
    },
    34: {
      TableName: "DEPARTMENT_Clocation",
      attributes: { Clocation: "str", DEPARTMENT_name: "str" },
      primaryKey: ["Clocation", "DEPARTMENT_name"],
      ForgeinKey: [
        {
          attributeName: "DEPARTMENT_name",
          ForignKeyTable: "DEPARTMENT",
          ForignKeyTableAttributeName: "name",
          patricipaction: "full",
          dataType: "str",
        },
      ],
      isWeak: false,
    },
    12: {
      TableName: "EMPLOYEE",
      attributes: {
        last_name: "str",
        middle_initis: "str",
        irst_name: "str",
        addres: "str",
        salary: "float",
        sex: "str",
        status: "str",
        birth_dat: "str",
        attr_1: "str",
        start_date: "datetime",
        DEPARTMENT_Employed_name: "str",
        EMPLOYEE_Supervision_attr_1: "str",
      },
      primaryKey: ["attr_1"],
      ForgeinKey: [
        {
          attributeName: "DEPARTMENT_Employed_name",
          ForignKeyTable: "DEPARTMENT",
          ForignKeyTableAttributeName: "name",
          patricipaction: "full",
          dataType: "str",
        },
        {
          attributeName: "EMPLOYEE_Supervision_attr_1",
          ForignKeyTable: "EMPLOYEE",
          ForignKeyTableAttributeName: "attr_1",
          patricipaction: "partial",
          dataType: "str",
        },
      ],
      isWeak: false,
    },
    24: {
      TableName: "PROJECT",
      attributes: {
        location: "str",
        attr_2: "str",
        budget: "float",
        DEPARTMENT_Assigned_name: "str",
      },
      primaryKey: ["attr_2"],
      ForgeinKey: [
        {
          attributeName: "DEPARTMENT_Assigned_name",
          ForignKeyTable: "DEPARTMENT",
          ForignKeyTableAttributeName: "name",
          patricipaction: "partial",
          dataType: "str",
        },
      ],
      isWeak: false,
    },
    25: {
      TableName: "DEPENDENT",
      attributes: {
        "90x": "str",
        relatlonship: "str",
        name: "str",
        birth_date: "datetime",
        Dependents_EMPLOYEE_attr_1: "str",
      },
      primaryKey: ["Dependents_EMPLOYEE_attr_1"],
      ForgeinKey: [
        {
          attributeName: "Dependents_EMPLOYEE_attr_1",
          ForignKeyTable: "EMPLOYEE",
          ForignKeyTableAttributeName: "attr_1",
          patricipaction: "partial",
          dataType: "str",
        },
      ],
      isWeak: true,
    },
    35: {
      TableName: "Works_EMPLOYEE_PROJECT",
      attributes: {
        start_date: "datetime",
        hours: "int",
        EMPLOYEE_attr_1: "str",
        PROJECT_attr_2: "str",
      },
      primaryKey: ["EMPLOYEE_attr_1", "PROJECT_attr_2"],
      ForgeinKey: [
        {
          attributeName: "EMPLOYEE_attr_1",
          ForignKeyTable: "EMPLOYEE",
          ForignKeyTableAttributeName: "attr_1",
          patricipaction: "full",
          dataType: "str",
        },
        {
          attributeName: "PROJECT_attr_2",
          ForignKeyTable: "PROJECT",
          ForignKeyTableAttributeName: "attr_2",
          patricipaction: "full",
          dataType: "str",
        },
      ],
      isWeak: false,
    },
  },
};

const mutations = {
  setErImage(state, image) {
    state.erImage = image;
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
  async getIpOutput({ commit, state }) {
    if (!state.ipOutPutReturned) {
      try {
        const response = await axios({
          method: "get",
          url: "/ipoutput",
          data: {},
        });
        commit("setIpOutputData", response.data);
        state.ipOutPutReturned = true;
        router.push("/ipOutput");
      } catch (err) {
        console.log(err);
      }
    }
  },
};
export default {
  namespaced: true,
  state,
  mutations,
  actions,
};
