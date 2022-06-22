
<template>
    <div id="home">
      <cardDesign 
      v-for="(card,i) in clusters"
          :key=i
          :title="card"
          :describtion= "''"
      />
    </div>
</template>

<script>
import cardDesign from '../components/cardDesign1.vue'
    export default{
    data() {
        return {
        clusters: ['c1', 'c2'],
        };
    },
  components: {
    cardDesign
    }
    };
</script>

<style lang='scss' scoped >
</style>
    