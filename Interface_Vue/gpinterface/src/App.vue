
<template>
    <div id="app">
      <cardDesign 
      v-for="(card,i) in clusters"
          :key=i
          :title="card"
          :describtion= "''"
      />
    </div>
</template>

<script>
import cardDesign from './components/cardDesign.vue'
    export default{
    data() {
        return {
        clusters: ['cluster1', 'cluster2', 'cluster3', 'cluster4'],
        };
    },
  components: {
    cardDesign
    }
    };
</script>

<style lang='scss' scoped >
    #app {
    font-size: 18px;
    font-family: 'Roboto', sans-serif;
    color: red;
    p{
        color: blue;
    }
    }
</style>
    