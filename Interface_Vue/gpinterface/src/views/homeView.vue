<template>
  <div class="home">
    <cardDesign
      title="Lorem ipsum"
      description="Lorem ipsum dolor sitUt enim ad
    minim veni ullamco laboris nisi ut aliquip ex ea commodo consequat Excepteur
    sint occaecat cupidatat non proident"
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
export default {
  components: {
    cardDesign,
    colorPallete,
  },
};
</script>
