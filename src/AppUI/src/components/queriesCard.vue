<template>
  <div class="queriesCard">
    <div class="controlBar">
      <div class="queryTitle">{{ queryName }}</div>
      <div class="queryControls">
        <div
          class="editIcon"
          :id="'editIcon' + this.id"
          @click="toggleEditQuery"
        >
          <i class="fa fa-edit"></i>
        </div>
        <div class="trashIcon" :id="'trashIcon' + this.id" @click="deleteQuery">
          <i class="fa fa-trash" aria-hidden="true"></i>
        </div>
      </div>
    </div>
    <div class="showQuery">
      <p>{{ query }}</p>
    </div>
    <div class="editQuery" :id="'editQuery' + this.id">
      <input
        type="text"
        :placeholder="this.queryName"
        v-model="updatedQueryName"
      />
      <textarea v-model="updatedQuery" :placeholder="this.query"></textarea>
      <div class="saveChangesBtn">
        <button class="customBtn" @click="saveChanges">Save Changes</button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/Colors.scss";
@import "../scss/Button.scss";
.queriesCard {
  width: 80%;
  margin: 40px;
  padding: 20px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  border-radius: 12px;
  transition: 0.5s;
}
.controlBar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid $lightBlue;
  padding-bottom: 20px;
  padding-top: 20px;
  .queryControls {
    display: flex;
  }
  .queryTitle {
    font-size: 30px;
    font-weight: 700;
    color: $darkBlue;
  }
}
.trashIcon,
.editIcon {
  margin-left: 12px;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background-color: $darkBlue;
  color: white;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.5);
  transition: all 0.3s ease 0s;
  &:hover {
    transform: translateY(-3px);
    background-color: $lightBlue;
  }
  i {
    font-size: 30px;
    padding: 9px;
    color: white;
    cursor: pointer;
  }
}
.trashIcon {
  i {
    padding: 9px;
    padding-left: 12px;
  }
}
.showQuery {
  padding-top: 20px;
  p {
    font-size: 30px;
    word-wrap: break-word;
  }
}
.editQuery {
  display: none;
  input {
    width: 100%;
    margin-bottom: 35px;
    padding: 10px;
    border: none;
    border-bottom: 2px solid $darkBlue;
    font-size: 27px;
    font-weight: 700;
    color: $darkBlue;
    &:focus {
      outline: none;
      border-bottom: 2px solid $lightBlue;
    }
  }
  textarea {
    padding: 12px;
    font-size: 22px;
    max-width: 100%;
    min-height: 200px;
    color: $darkBlue;
    border: 1px solid $darkBlue;
    &:focus {
      outline: none;
      border: 2px solid $lightBlue;
    }
  }
  .saveChangesBtn {
    padding-top: 20px;
    display: flex;
    justify-content: flex-end;
  }
}
@media screen and (max-width: 768px) {
  .controlBar {
    flex-wrap: wrap-reverse;
    .queryControls {
      margin-left: auto;
      margin-bottom: 20px;
    }
  }
}
</style>

<script>
export default {
  name: "queriesCard",
  data() {
    return {
      updatedQueryName: "",
      updatedQuery: "",
    };
  },
  props: {
    queryName: {
      type: String,
      required: true,
    },
    query: {
      type: String,
      required: true,
    },
    id: {
      type: String,
      required: true,
    },
  },
  methods: {
    saveChanges() {
      if (this.updatedQueryName === "") {
        this.updatedQueryName = this.queryName;
      }
      if (this.updatedQuery === "") {
        this.updatedQuery = this.query;
      }
      this.$store.commit("predictedQueries/editQuery", {
        query: this.updatedQuery,
        queryName: this.updatedQueryName,
        oldQuery: this.query,
        oldQueryName: this.queryName,
      });
      this.toggleEditQuery();
    },
    toggleEditQuery() {
      let editQuery = document.getElementById("editQuery" + this.id);
      if (editQuery.style.display === "flex") {
        editQuery.style.display = "none";
      } else {
        editQuery.style.display = "flex";
        editQuery.style.flexDirection = "column";
      }
    },
    deleteQuery() {
      this.$store.commit("predictedQueries/setDeletedQuery", {
        query: this.query,
        queryName: this.queryName,
      });
      this.$store.commit("triggerModals/toggleDeleteQueryModal");
    },
  },
};
</script>
