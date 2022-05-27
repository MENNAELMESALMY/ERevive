<template>
  <div id="app">
    <h1>Welcome in Erevive :)</h1>
    <card-wrapper
      :cardsColor="cardsColor"
      :cardsData="cardsData"
    ></card-wrapper>
    <card-with-options :colorHex="cardWithOptions.colorHex"></card-with-options>
  </div>
</template>
<style lang="scss">
html,
body {
  margin: 0;
  padding: 0;
}
</style>

<script>
import CardWrapper from "./components/cardWrapper.vue";
import CardWithOptions from "./components/cards/cardWithOptions.vue";

export default {
  name: "App",
  data: function () {
    return {
      cardsData: [
        {
          title: "Menna Card1",
          buttonText: "Read More",
          text: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book Lorem Ipsum is simply dummy text of the printing and typesetting industry. Standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book",
        },
        {
          title: "Menna Card1 Again",
          buttonText: "Read More",
          text: "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book",
        },
        {
          title: "Menna Card1 Again Again",
          buttonText: "Read More",
          text: "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
        },
        {
          title: "Menna Card1 Again Again Again Again Again Again Again",
          buttonText: "Read More",
          text: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book Lorem Ipsum is simply dummy text of the printing and typesetting industry. Standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book",
        },
      ],
      cardsColor: "#C26DBC",
      cardWithOptions: {
        title: "Menna Card 2",
        subData: [
          {
            subtitle: "Subtitle 1",
            text: "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
          },
          {
            subtitle: "Subtitle 2",
            text: "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
          },
          {
            subtitle: "Subtitle 3",
            text: "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
          },
        ],
        colorHex: "#EEB5EB",
      },
    };
  },
  components: {
    CardWrapper,
    CardWithOptions,
  },
};
</script>
