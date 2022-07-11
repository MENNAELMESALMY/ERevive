import axios from "axios";
const state = {
  //   schema: {},
  schema: {
    11: {
      TableName: "DEPARTMENT",
      TableType: "",
      attributes: {
        name: "str",
        start_date: "datetime",
        EMPLOYEE_Manages: "str",
      },
      primaryKey: ["name"],
      ForgeinKey: [
        {
          attributeName: "EMPLOYEE_Manages",
          ForignKeyTable: "EMPLOYEE",
          ForignKeyTableAttributeName: "ssn",
          patricipaction: "partial",
          dataType: "str",
        },
      ],
      isWeak: false,
    },
    34: {
      TableName: "DEPARTMENT_Clocation",
      TableType: "",
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
      TableType: "",
      attributes: {
        last_name: "str",
        middle_initis: "str",
        first_name: "str",
        address: "str",
        salary: "float",
        sex: "str",
        status: "str",
        birth_dat: "str",
        ssn: "str",
        start_date: "datetime",
        DEPARTMENT_Employed_name: "str",
        EMPLOYEE_Supervision_: "str",
      },
      primaryKey: ["ssn"],
      ForgeinKey: [
        {
          attributeName: "DEPARTMENT_Employed_name",
          ForignKeyTable: "DEPARTMENT",
          ForignKeyTableAttributeName: "name",
          patricipaction: "full",
          dataType: "str",
        },
        {
          attributeName: "EMPLOYEE_Supervision_",
          ForignKeyTable: "EMPLOYEE",
          ForignKeyTableAttributeName: "ssn",
          patricipaction: "partial",
          dataType: "str",
        },
      ],
      isWeak: false,
    },
    24: {
      TableName: "PROJECT",
      TableType: "",
      attributes: {
        location: "str",
        name: "str",
        budget: "float",
        DEPARTMENT_Assigned_name: "str",
      },
      primaryKey: ["name"],
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
      TableType: "",
      attributes: {
        sex: "str",
        relatlonship: "str",
        name: "str",
        birth_date: "datetime",
        Dependents_EMPLOYEE_: "str",
      },
      primaryKey: ["Dependents_EMPLOYEE_"],
      ForgeinKey: [
        {
          attributeName: "Dependents_EMPLOYEE_",
          ForignKeyTable: "EMPLOYEE",
          ForignKeyTableAttributeName: "ssn",
          patricipaction: "partial",
          dataType: "str",
        },
      ],
      isWeak: true,
    },
    35: {
      TableName: "Works_EMPLOYEE_PROJECT",
      TableType: "mTm",
      attributes: {
        start_date: "datetime",
        hours: "int",
        EMPLOYEE_: "str",
        PROJECT_: "str",
      },
      primaryKey: ["EMPLOYEE_", "PROJECT_"],
      ForgeinKey: [
        {
          attributeName: "EMPLOYEE_",
          ForignKeyTable: "EMPLOYEE",
          ForignKeyTableAttributeName: "ssn",
          patricipaction: "full",
          dataType: "str",
        },
        {
          attributeName: "PROJECT_",
          ForignKeyTable: "PROJECT",
          ForignKeyTableAttributeName: "name",
          patricipaction: "full",
          dataType: "str",
        },
      ],
      isWeak: false,
    },
  },
  formData:{}
};
const actions = {
  async sendSchema({ state }, payload) {
    let schema = {
        "schema": payload.finalSchema,
    }
    state.formData = payload.formData;
    try {
      await axios.post("/searchengine", schema);
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
