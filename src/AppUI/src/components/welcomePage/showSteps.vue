<template>
  <div class="showSteps">
    <stepsCard
      v-for="(card, i) in cards"
      :key="i"
      :title="card.title"
      :description="card.description"
      :image="card.image"
      :direction="card.direction"
    />
  </div>
</template>

<style lang="scss" scoped></style>

<script>
import stepsCard from "./stepsCard.vue";
export default {
  name: "showSteps",
  data() {
    return {
      cards: [
        {
          title: "1. Upload Image",
          description: "Upload ER Diagram Image",
          image: require("../../../public/assets/dummyImage.png"),
          direction: "right",
        },
        {
          title: "2. Analyze Image",
          description:
            "Extract information from the image (Entities, attributes and relations)",
          image: require("../../../public/assets/dummyImage.png"),
          direction: "left",
        },
        {
          title: "3. Validate Output",
          description: "Validate the extracted information from the image",
          image: require("../../../public/assets/dummyImage.png"),
          direction: "right",
        },
        {
          title: "4. Generating SQL Queries",
          description: "Generate top ranked sql queries for your system",
          image: require("../../../public/assets/dummyImage.png"),
          direction: "left",
        },
        {
          title: "5. Create Backend Application",
          description: "Create backend application with Flask and SQL Alchemy",
          image: require("../../../public/assets/dummyImage.png"),
          direction: "right",
        },
        {
          title: "6. Create Frontend Application",
          description: "Create Frontend application with Vue and Vuex",
          image: require("../../../public/assets/dummyImage.png"),
          direction: "left",
        },
      ],
    };
  },
  components: {
    stepsCard,
  },
};
</script>
