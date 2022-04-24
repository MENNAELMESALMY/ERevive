<template>
  <div class="home">
    <cardDesign
      title="Lorem ipsum"
      description="Lorem ipsum dolor sitUt enim ad
    minim veni ullamco laboris nisi ut aliquip ex ea commodo consequat Excepteur
    sint occaecat cupidatat non proident"
    />
    <cardDesign2
      title="Lorem ipsum"
      description="Lorem ipsum dolor sitUt enim ad laboris nisi ut aliquip ex ea commodo"
    />
    <cardDesign3
      title="Lorem ipsum"
      description="Lorem ipsum dolor sitUt enim ad laboris nisi ut aliquip ex ea commodo"
    />
    <colorPallete />
  </div>
</template>

<style lang="scss" scoped>
.home {
  padding: 30px;
}
</style>

<script>
import cardDesign from "../components/cardDesign.vue";
import colorPallete from "../components/colorPallete.vue";
import cardDesign2 from "../components/cardDesign2.vue";
import cardDesign3 from "../components/cardDesign3.vue";
export default {
  components: {
    cardDesign,
    colorPallete,
    cardDesign2,
    cardDesign3,
  },
};
</script>
