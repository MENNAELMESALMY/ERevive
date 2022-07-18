<template>
  <div class="nlpToSql">
    <div class="subTitle">Do You Want to Convert NLP To SQL ?</div>
    <textarea
      class="enterNlp"
      placeholder="Enter your question here ..."
      v-model="nlpQuestion"
    ></textarea>
    <div class="subTitle">Generated SQL Query</div>
    <textarea v-model="generatedSql"></textarea>
    <button class="customBtn" @click="convertNlpToSql">
      Convert NLP To SQL
    </button>
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/Colors.scss";
@import "../scss/Button.scss";
.nlpToSql {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  width: 100%;
  .subTitle {
    margin-top: 50px;
    padding: 20px;
    font-size: 45px;
    font-weight: 700;
    font-family: "Indie Flower", cursive;
    text-align: center;
    color: $darkBlue;
  }
  textarea {
    padding: 12px;
    font-size: 30px;
    margin-top: 30px;
    width: 80%;
    max-width: 100%;
    min-height: 200px;
    color: $darkBlue;
    border: 1px solid $darkBlue;
    &:focus {
      outline: none;
      border: 2px solid $lightBlue;
    }
  }
  .customBtn {
    margin-top: 40px;
    margin-bottom: 20px;
    width: 50%;
  }
}
@media screen and (max-width: 768px) {
  .nlpToSql {
    .customBtn {
      width: 80%;
    }
  }
}
</style>

<script>
import { mapState } from "vuex";
export default {
  name: "nlpToSql",
  data() {
    return {
      nlpQuestion: "",
    };
  },
  computed: {
    ...mapState({
      generatedSql: (state) => state.predictedQueries.generatedSql,
    }),
  },
  methods: {
    convertNlpToSql() {
      this.$store.dispatch("predictedQueries/postConvertNlpToSql", {
        nlpQuestion: this.nlpQuestion,
      });
      this.nlpQuestion.value = "";
    },
  },
};
</script>
