<template>
  <div class="card_wrapper">
    <card-with-tag
      v-for="card in cardsData"
      :key="card.id"
      :title="card.title"
      :text="card.text"
      :color-hex="cardsColor"
      :button-text="card.buttonText"
    ></card-with-tag>
  </div>
</template>
<style lang="scss">
.card_wrapper {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  padding: 0 100px;
}
</style>

<script>
import CardWithTag from "./cards/cardWithTag.vue";

export default {
  name: "CardWrapper",
  props: {
    cardsColor: { type: String },
    cardsData: { type: Array },
  },
  components: {
    CardWithTag,
  },
};
</script>
