<template>
  <div class="showSteps">
    <div
      id="carouselExampleIndicators"
      class="carousel slide"
      data-ride="carousel"
    >
      <ol class="carousel-indicators">
        <li
          data-target="#carouselExampleIndicators"
          data-slide-to="0"
          class="active"
        ></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="3"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="4"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="5"></li>
      </ol>
      <div class="carousel-inner">
        <steps-card
          class="carousel-item active"
          title="1. Upload Image"
          description="Upload your ER diagram image"
        />
        <steps-card
          class="carousel-item"
          v-for="(card, i) in cards"
          :key="i"
          :title="card.title"
          :description="card.description"
        />
      </div>
      <a
        class="carousel-control-prev"
        href="#carouselExampleIndicators"
        role="button"
        data-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a
        class="carousel-control-next"
        href="#carouselExampleIndicators"
        role="button"
        data-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.carousel-inner {
  align-items: center;
}
#carouselExampleIndicators {
  width: 70%;
  margin: auto;
}
@media screen and (max-width: 500px) {
  #carouselExampleIndicators {
    width: 90%;
  }
}
</style>

<script>
import stepsCard from "./stepsCard.vue";
export default {
  name: "showSteps",
  data() {
    return {
      cards: [
        {
          title: "2. Analyze Image",
          description:
            "Extract information from the image (Entities, attributes and relations)",
        },
        {
          title: "3. Validate Output",
          description: "Validate the extracted information from the image",
        },
        {
          title: "4. Generating SQL Queries",
          description: "Generate top ranked sql queries for your system",
        },
        {
          title: "5. Create Backend Application",
          description: "Create backend application with Flask and SQL Alchemy",
        },
        {
          title: "6. Create Frontend Application",
          description: "Create Frontend application with Vue and Vuex",
        },
      ],
    };
  },
  components: {
    stepsCard,
  },
};
</script>
