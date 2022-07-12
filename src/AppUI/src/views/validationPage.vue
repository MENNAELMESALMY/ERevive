<template>
  <div class="validation">
    <h2 class="subTitle">validation</h2>
    <div class="entities_names_wrapper" :key="componentKey + 4000">
      <div class="entities_names">
        <a
          v-for="(value, entityIdx) in globalSchema"
          :key="value['TableName']"
          :href="'#' + globalSchema[entityIdx]['TableName']"
        >
          {{ globalSchema[entityIdx]["TableName"] }}
        </a>
      </div>
    </div>

    <div
      v-for="(value, entityIdx) in globalSchema"
      :key="entityIdx"
      class="entity_card"
      :id="globalSchema[entityIdx]['TableName']"
    >
      <div class="close_wrapper" v-if="Object.keys(globalSchema).length > 1">
        <i
          class="fa fa-times close"
          id="close"
          @click="delete_entity(entityIdx)"
        ></i>
      </div>
      <h3 class="subTitle" :key="componentKey + entityIdx">
        {{ globalSchema[entityIdx]["TableName"] }}
      </h3>
      <form class="entity_form">
        <input
          type="text"
          v-model="globalSchema[entityIdx]['TableName']"
          required
          @input="change_name"
          :id="entityIdx + '_entity_name'"
        />
        <div>
          <input
            type="checkbox"
            v-model="globalSchema[entityIdx]['isWeak']"
            required
          />
          <span>isWeak</span>
        </div>
        <!-- < attributes /> -->
        <div class="attributes_wrapper">
          <div
            v-for="(attr, index) in globalSchema[entityIdx]['attributes']"
            :key="index"
            class="attribute_card"
          >
            <div
              class="close_wrapper"
              v-if="
                Object.keys(globalSchema[entityIdx]['attributes']).length > 1
              "
            >
              <i
                class="fa fa-times close"
                id="close"
                @click="delete_attr(entityIdx, index)"
              ></i>
            </div>
            <!-- <input v-model="globalSchema[entityIdx]['attributes'][index][0]" />
            <select v-model="globalSchema[entityIdx]['attributes'][index][1]"> -->
            <input
              type="text"
              @input="change_name"
              :id="entityIdx + '_' + index + '_attr_name'"
              v-model="attr[0]"
              required
            />
            <select v-model="attr[1]">
              <option
                v-for="dataType in dataTypes"
                :value="dataType"
                :key="dataType"
              >
                {{ dataType }}
              </option>
            </select>
            <select v-model="attr[3]">
              <option
                v-for="fieldType in fieldTypes"
                :value="fieldType"
                :key="fieldType"
              >
                {{ fieldType }}
              </option>
            </select>
            <div v-if="requireOptions.includes(attr[3])">
              <p>Enter list of options as comma separated string</p>
              <input type="text" v-model="attr[4]" />
              <!-- <input @change="change_name" type="text" v-model="attr[4]" /> -->
            </div>
            <div v-if="attr[3] == 'number'">
              <label>Minimum number</label>
              <!-- <input @change="change_name" v-model="attr[5]" type="number" /> -->
              <input v-model="attr[5]" type="number" />
            </div>

            <div v-if="attr[3] == 'number'">
              <label>Maximum number</label>
              <!-- <input @change="change_name" v-model="attr[6]" type="number" /> -->
              <input v-model="attr[6]" type="number" />
            </div>

            <div>
              <input
                type="checkbox"
                v-model="attr[2]"
                @change="componentKey = (componentKey + 1) % 2"
                required
              />
              <span>isPrimary</span>
            </div>
          </div>
        </div>
        <button class="customBtn" @click="add_attribute(entityIdx)">
          Add Attribute
        </button>
        <!-- < foreign keys /> -->
        <div class="fks_wrapper" :key="componentKey + 2000">
          <div
            v-for="(fk, fkIndex) in globalSchema[entityIdx]['ForgeinKey']"
            :key="fkIndex"
            class="fk_card"
          >
            <div class="close_wrapper">
              <i
                class="fa fa-times close"
                id="close"
                @click="delete_fk(entityIdx, fkIndex)"
              ></i>
            </div>
            <select v-model="fk['attributeIdx']">
              <option
                v-for="(attr, idx) in globalSchema[entityIdx]['attributes']"
                :value="idx"
                :key="idx"
              >
                {{ attr[0] }}
              </option>
            </select>

            <select
              v-model="fk['ForignKeyTableIdx']"
              @change="fk['ForignKeyTableAttributeIdx'] = 0"
            >
              <option
                v-for="(
                  fkEntityValue, fkEntityKey, fkEntityIdx
                ) in globalSchema"
                :value="fkEntityIdx"
                :key="fkEntityIdx"
              >
                {{ fkEntityValue["TableName"] }}
              </option>
            </select>

            <select v-model="fk['ForignKeyTableAttributeIdx']">
              <option
                v-for="(fkEntityAttrValue, fkEntityAttrIdx) in globalSchema[
                  fk['ForignKeyTableIdx']
                ]['attributes']"
                :value="fkEntityAttrIdx"
                :key="fkEntityAttrIdx"
                :disabled="!fkEntityAttrValue[2]"
              >
                {{ fkEntityAttrValue[0] }}
              </option>
            </select>

            <select v-model="fk['patricipaction']">
              <option v-for="p in patricipations" :value="p" :key="p">
                {{ p }}
              </option>
            </select>
          </div>
        </div>

        <button class="customBtn" @click="add_fk(entityIdx)">
          Add Foreign Key
        </button>
      </form>
    </div>
    <div class="error_wrapper" v-if="errors.length > 0">
      <p v-for="(e, idx) in errors" :value="e" :key="idx" class="error">
        {{ e }}
      </p>
    </div>
    <div class="button_wrapper">
      <button class="customBtn" @click="add_entity">Add Entity</button>
      <button class="customBtn" @click="save_changes">Save changes</button>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/Colors.scss";
@import "../scss/validation.scss";
</style>

<script>
import { mapState } from "vuex";

export default {
  name: "validationPage",
  data: function () {
    return {
      componentKey: 0,
      entityCount: 0,
      dataTypes: ["str", "int", "float", "datetime", "bool"],
      patricipations: ["full", "partial"],
      fieldTypes: [
        "text",
        "number",
        "date",
        "email",
        "password",
        "tel",
        "url",
        "checkbox",
        "list",
        "radiobutton",
        "textarea",
      ],
      requireOptions: ["checkbox", "list", "radiobutton"],
      globalSchema: {},
      finalSchema: {},
      formData: {},
      errors: [],
    };
  },
  methods: {
    add_entity() {
      this.entityCount =
        parseInt(Object.keys(this.globalSchema).slice(-1)[0]) + 1;
      let name = "new_entity" + this.entityCount;
      this.globalSchema[this.entityCount] = {
        TableName: name,
        TableType: "",
        attributes: { 0: ["default_pk", "str", true, "text", "", 0, 100] },
        primaryKey: [],
        ForgeinKey: [],
        isWeak: false,
      };
      this.componentKey = (this.componentKey + 1) % 2;
    },
    change_name() {
      this.componentKey = (this.componentKey + 1) % 2;
      // const el_id = event.target.id;
      // document.getElementById(el_id).focus();
      // setTimeout(function () {
      //   document.getElementById(el_id).focus();
      // }, 0);
    },
    delete_entity(entityIdx) {
      for (let key in this.globalSchema) {
        for (let fk in this.globalSchema[key]["ForgeinKey"]) {
          let ForignKeyTableIdx =
            this.globalSchema[key]["ForgeinKey"][fk]["ForignKeyTableIdx"];
          if (ForignKeyTableIdx == entityIdx) {
            this.delete_fk(key, fk);
          }
        }
      }
      delete this.globalSchema[entityIdx];
      this.componentKey = (this.componentKey + 1) % 2;
    },
    save_changes() {
      this.finalSchema = {};
      this.formData = {};
      for (let key in this.globalSchema) {
        let TableName = this.globalSchema[key]["TableName"];
        this.formData[TableName] = [];
        this.finalSchema[TableName] = {
          TableName: TableName,
          TableType: "",
          attributes: {},
          primaryKey: [],
          ForgeinKey: [],
          isWeak: this.globalSchema[key]["isWeak"],
        };
        for (let attr in this.globalSchema[key]["attributes"]) {
          let attrName = this.globalSchema[key]["attributes"][attr][0];
          let attrDataType = this.globalSchema[key]["attributes"][attr][1];
          let attrIsPrimaryKey = this.globalSchema[key]["attributes"][attr][2];
          let fieldType = this.globalSchema[key]["attributes"][attr][3];
          let listOfValues = this.globalSchema[key]["attributes"][attr][4];
          let minNum = this.globalSchema[key]["attributes"][attr][5];
          let maxNum = this.globalSchema[key]["attributes"][attr][6];
          this.finalSchema[TableName]["attributes"][attrName] = attrDataType;

          if (attrIsPrimaryKey)
            this.finalSchema[TableName]["primaryKey"].push(attrName);

          this.formData[TableName].push({
            field_name: attrName,
            field_type: fieldType,
            data_type: attrDataType,
            isRequired: true,
            maxRange: parseInt(maxNum),
            minRange: parseInt(minNum),
            options: listOfValues.split(","),
          });
        }
        for (let fk in this.globalSchema[key]["ForgeinKey"]) {
          let ForignKeyTableIdx =
            this.globalSchema[key]["ForgeinKey"][fk]["ForignKeyTableIdx"];
          let attributeIdx =
            this.globalSchema[key]["ForgeinKey"][fk]["attributeIdx"];
          let ForignKeyTableAttributeIdx =
            this.globalSchema[key]["ForgeinKey"][fk][
              "ForignKeyTableAttributeIdx"
            ];
          let ForignKeyTableName =
            this.globalSchema[ForignKeyTableIdx]["TableName"];
          let attributeName =
            this.globalSchema[key]["attributes"][attributeIdx][0];
          let ForignKeyTableAttributeName =
            this.globalSchema[ForignKeyTableIdx]["attributes"][
              ForignKeyTableAttributeIdx
            ][0];
          let patricipaction =
            this.globalSchema[key]["ForgeinKey"][fk]["patricipaction"];
          let dataType = this.globalSchema[key]["attributes"][attributeIdx][1];
          this.finalSchema[TableName]["ForgeinKey"].push({
            attributeName: attributeName,
            ForignKeyTable: ForignKeyTableName,
            ForignKeyTableAttributeName: ForignKeyTableAttributeName,
            patricipaction: patricipaction,
            dataType: dataType,
          });
        }
      }
      console.log("finalSchema", this.finalSchema);
      let isValid = this.check_validation();
      if (isValid) {
        // send request to server
        // console.log("validation success");
        let payload = {
          finalSchema: this.finalSchema,
          formData: this.formData,
        };
        this.$store.dispatch(
          "predictedQueries/postSearchEngineQueries",
          payload
        );
        this.$store.commit(
          "predictedQueries/setLoadingTitle",
          "Suggesting Queries ..."
        );
        this.$router.push("/loadingPage");
      } else {
        console.log("validation failed");
      }
    },
    add_attribute(entityIdx) {
      let nxtIdx =
        parseInt(
          Object.keys(this.globalSchema[entityIdx]["attributes"]).slice(-1)[0]
        ) + 1;
      let attrName = "attribute_" + nxtIdx;
      this.globalSchema[entityIdx]["attributes"][nxtIdx] = [
        attrName,
        "str",
        false,
        "text",
        "",
        0,
        100,
      ];
      this.componentKey = (this.componentKey + 1) % 2;
    },
    delete_attr(entityIdx, attributeIdx) {
      // console.log("del atte", entityIdx, attributeIdx);
      for (let key in this.globalSchema) {
        for (let fk in this.globalSchema[key]["ForgeinKey"]) {
          let TableIdx = this.globalSchema[key]["ForgeinKey"][fk]["TableIdx"];
          let ForignKeyTableIdx =
            this.globalSchema[key]["ForgeinKey"][fk]["ForignKeyTableIdx"];
          let ForignKeyTableAttributeIdx =
            this.globalSchema[key]["ForgeinKey"][fk][
              "ForignKeyTableAttributeIdx"
            ];
          let fkattributeIdx =
            this.globalSchema[key]["ForgeinKey"][fk]["attributeIdx"];
          if (
            (ForignKeyTableAttributeIdx == attributeIdx &&
              ForignKeyTableIdx == entityIdx) ||
            (fkattributeIdx == attributeIdx && TableIdx == entityIdx)
          )
            this.delete_fk(key, fk);
        }
      }
      delete this.globalSchema[entityIdx]["attributes"][attributeIdx];
      this.componentKey = (this.componentKey + 1) % 2;
    },
    add_fk(entityIdx) {
      let fk = {
        attributeIdx: 0,
        ForignKeyTableIdx: 0,
        ForignKeyTableAttributeIdx: 0,
        patricipaction: "full",
      };
      this.globalSchema[entityIdx]["ForgeinKey"].push(fk);
      this.componentKey = (this.componentKey + 1) % 2;
    },
    delete_fk(entityIdx, fkIndex) {
      this.globalSchema[entityIdx]["ForgeinKey"].splice(fkIndex, 1);
      this.componentKey = (this.componentKey + 1) % 2;
    },
    check_validation() {
      this.errors = [];
      for (let key in this.finalSchema) {
        let TableName = this.finalSchema[key]["TableName"];
        let attributes = this.finalSchema[key]["attributes"];
        let primaryKey = this.finalSchema[key]["primaryKey"];
        let ForgeinKey = this.finalSchema[key]["ForgeinKey"];
        if (TableName == "") {
          this.errors.push("TableName is empty");
          continue;
        }
        for (let attr in attributes)
          if (attr == "")
            this.errors.push(
              "AttributeName in Table " + TableName + " is empty"
            );

        if (primaryKey.length == 0)
          this.errors.push("Table " + TableName + " has no primary key");
        for (let fk in ForgeinKey) {
          let attributeName = ForgeinKey[fk]["attributeName"];
          let ForignKeyTable = ForgeinKey[fk]["ForignKeyTable"];
          let ForignKeyTableAttributeName =
            ForgeinKey[fk]["ForignKeyTableAttributeName"];
          if (
            this.finalSchema[ForignKeyTable]["attributes"][
              ForignKeyTableAttributeName
            ] != attributes[attributeName]
          ) {
            this.errors.push(
              "Attribute " +
                attributeName +
                " in Table " +
                TableName +
                " has datatype mismatch "
            );
          }
        }
      }
      for (let key in this.formData) {
        for (let attrIdx in this.formData[key]) {
          // check if data type is compatible with the attribute type
          let attrName = this.formData[key][attrIdx]["field_name"];
          let attrType = this.formData[key][attrIdx]["field_type"];
          let dataType = this.formData[key][attrIdx]["data_type"];
          let maxRange = this.formData[key][attrIdx]["maxRange"];
          let minRange = this.formData[key][attrIdx]["minRange"];
          let options = this.formData[key][attrIdx]["options"];
          if (attrType == "number")
            if (dataType != "int" && dataType != "float") {
              this.errors.push(
                "Attribute1 " +
                  attrName +
                  " " +
                  attrType +
                  " " +
                  dataType +
                  " " +
                  " in Table " +
                  key +
                  " has datatype mismatch with formData type"
              );
            }

          if (dataType == "int" || dataType == "float")
            if (attrType != "number") {
              this.errors.push(
                "Attribute " +
                  attrName +
                  " " +
                  attrType +
                  " " +
                  dataType +
                  " " +
                  " in Table " +
                  key +
                  " has datatype mismatch with formData type"
              );
            }

          if (
            (attrType == "date" && dataType != "datetime") ||
            (dataType == "datetime" && attrType != "date")
          ) {
            this.errors.push(
              "Attribute " +
                attrName +
                " " +
                attrType +
                " " +
                dataType +
                " in Table " +
                key +
                " has datatype mismatch with formData type"
            );
          }

          if (attrType == "number" && minRange >= maxRange)
            this.errors.push(
              "Attribute " +
                attrName +
                " in table " +
                key +
                " has invalid range"
            );
          if (this.requireOptions.includes(attrType) && options.length <= 1)
            this.errors.push(
              "Attribute " + attrName + " in table " + key + " has no options"
            );
        }
      }
      // check dataType validation
      return this.errors.length == 0;
    },
  },
  beforeMount() {
    //await this.$store.dispatch("validation/getSchema");
    let entityIndex = 0;
    let invertedNamesList = {};
    for (let key in this.receivedSchema) {
      let TableName = this.receivedSchema[key]["TableName"];
      invertedNamesList[TableName] = { idx: entityIndex };
      // console.log(TableName, key);
      invertedNamesList[TableName]["attributes"] = {};
      let attrIndex = 0;
      for (let attr in this.receivedSchema[key]["attributes"]) {
        // console.log(attrIndex, attr);
        invertedNamesList[TableName]["attributes"][attr] = attrIndex;
        attrIndex += 1;
      }
      entityIndex += 1;
    }
    for (let key in this.receivedSchema) {
      let TableName = this.receivedSchema[key]["TableName"];
      let attributes = this.receivedSchema[key]["attributes"];
      let primaryKey = this.receivedSchema[key]["primaryKey"];
      let ForgeinKey = this.receivedSchema[key]["ForgeinKey"];
      let TableIdx = invertedNamesList[TableName]["idx"];
      this.globalSchema[TableIdx] = {
        TableName: TableName,
        attributes: {},
        ForgeinKey: [],
        isWeak: this.receivedSchema[key]["isWeak"],
      };
      let attrIndex = 0;
      for (let attr in attributes) {
        this.globalSchema[TableIdx]["attributes"][attrIndex] = [
          attr,
          attributes[attr],
          primaryKey.includes(attr),
          "text",
          "",
          0,
          100,
        ];
        attrIndex += 1;
      }
      for (let fk in ForgeinKey) {
        // console.log("fk", fk);
        let attributeName = ForgeinKey[fk]["attributeName"];
        let ForignKeyTable = ForgeinKey[fk]["ForignKeyTable"];
        let ForignKeyTableAttributeName =
          ForgeinKey[fk]["ForignKeyTableAttributeName"];
        let ForignKeyTableIdx = invertedNamesList[ForignKeyTable]["idx"];
        let ForignKeyTableAttributeIdx =
          invertedNamesList[ForignKeyTable]["attributes"][
            ForignKeyTableAttributeName
          ];
        let attributeIdx =
          invertedNamesList[TableName]["attributes"][attributeName];
        this.globalSchema[TableIdx]["ForgeinKey"].push({
          attributeName: attributeName,
          ForignKeyTable: ForignKeyTable,
          ForignKeyTableAttributeName: ForignKeyTableAttributeName,
          attributeIdx: attributeIdx,
          ForignKeyTableIdx: ForignKeyTableIdx,
          ForignKeyTableAttributeIdx: ForignKeyTableAttributeIdx,
          patricipaction: ForgeinKey[fk]["patricipaction"],
        });
      }
    }
    this.componentKey = (this.componentKey + 1) % 2;
  },
  computed: {
    ...mapState({
      receivedSchema: (state) => state.systemInput.initialSchema,
    }),
  },
};
</script>
