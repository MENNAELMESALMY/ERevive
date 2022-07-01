
<template>
    <div>
    
      <get-players-filteredby-playerID-groupedby-all/>
      
      <get-players-filteredby-height-groupedby-all/>
      
      <get-players-filteredby-weight-groupedby-all/>
      
      <get-players-groupedby-all/>
      
    </div>
</template>

    <style lang="scss" scoped>
    .home {
    padding: 30px;
    }
    </style>

    <script>
    
      import getPlayersFilteredbyPlayeridGroupedbyAll from '../components/get_players_filteredby_playerID_groupedby_all.vue'
      
      import getPlayersFilteredbyHeightGroupedbyAll from '../components/get_players_filteredby_height_groupedby_all.vue'
      
      import getPlayersFilteredbyWeightGroupedbyAll from '../components/get_players_filteredby_weight_groupedby_all.vue'
      
      import getPlayersGroupedbyAll from '../components/get_players_groupedby_all.vue'
      
export default {
  components: {
    
      getPlayersFilteredbyPlayeridGroupedbyAll,
      
      getPlayersFilteredbyHeightGroupedbyAll,
      
      getPlayersFilteredbyWeightGroupedbyAll,
      
      getPlayersGroupedbyAll,
      
  },
};
</script>
    