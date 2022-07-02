
<template>
    <div>
    
      <get-awards-players-filteredby-year-groupedby-all/>
      
      <get-awards-players-groupedby-all/>
      
      <get-awards-players-groupedby-playerID-lgID/>
      
      <get-awards-players-filteredby-lgID-year-groupedby-year/>
      
      <get-awards-players-groupedby-playerID-orderedby-all/>
      
      <get-awards-players-orderedby-all/>
      
    </div>
</template>

    <style lang="scss" scoped>
    .home {
    padding: 30px;
    }
    </style>

    <script>
    
      import getAwardsPlayersFilteredbyYearGroupedbyAll from '../components/get_awards_players_filteredby_year_groupedby_all.vue'
      
      import getAwardsPlayersGroupedbyAll from '../components/get_awards_players_groupedby_all.vue'
      
      import getAwardsPlayersGroupedbyPlayeridLgid from '../components/get_awards_players_groupedby_playerID_lgID.vue'
      
      import getAwardsPlayersFilteredbyLgidYearGroupedbyYear from '../components/get_awards_players_filteredby_lgID_year_groupedby_year.vue'
      
      import getAwardsPlayersGroupedbyPlayeridOrderedbyAll from '../components/get_awards_players_groupedby_playerID_orderedby_all.vue'
      
      import getAwardsPlayersOrderedbyAll from '../components/get_awards_players_orderedby_all.vue'
      
export default {
  components: {
    
      getAwardsPlayersFilteredbyYearGroupedbyAll,
      
      getAwardsPlayersGroupedbyAll,
      
      getAwardsPlayersGroupedbyPlayeridLgid,
      
      getAwardsPlayersFilteredbyLgidYearGroupedbyYear,
      
      getAwardsPlayersGroupedbyPlayeridOrderedbyAll,
      
      getAwardsPlayersOrderedbyAll,
      
  },
};
</script>
    