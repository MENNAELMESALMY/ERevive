
<template>
    <div>
    
      <get-players-awards-players-filteredby-playerID-groupedby-all/>
      
      <get-awards-players-players-groupedby-birthCity-playerID-firstName-birthCountry-middleName-orderedby-all/>
      
      <get-players-awards-players-groupedby-all/>
      
      <get-awards-players-players-filteredby-year/>
      
      <get-players-awards-players-groupedby-playerID/>
      
      <get-players-awards-players-groupedby-playerID-lgID-orderedby-all/>
      
      <get-awards-players-players-filteredby-firstName-middleName-groupedby-playerID/>
      
      <get-players-awards-players-groupedby-hsCity-playerID-year-orderedby-all/>
      
      <get-awards-players-players-filteredby-height/>
      
    </div>
</template>

    <style lang="scss" scoped>
    .home {
    padding: 30px;
    }
    </style>

    <script>
    
      import getPlayersAwardsPlayersFilteredbyPlayeridGroupedbyAll from '../components/get_players_awards_players_filteredby_playerID_groupedby_all.vue'
      
      import getAwardsPlayersPlayersGroupedbyBirthcityPlayeridFirstnameBirthcountryMiddlenameOrderedbyAll from '../components/get_awards_players_players_groupedby_birthCity_playerID_firstName_birthCountry_middleName_orderedby_all.vue'
      
      import getPlayersAwardsPlayersGroupedbyAll from '../components/get_players_awards_players_groupedby_all.vue'
      
      import getAwardsPlayersPlayersFilteredbyYear from '../components/get_awards_players_players_filteredby_year.vue'
      
      import getPlayersAwardsPlayersGroupedbyPlayerid from '../components/get_players_awards_players_groupedby_playerID.vue'
      
      import getPlayersAwardsPlayersGroupedbyPlayeridLgidOrderedbyAll from '../components/get_players_awards_players_groupedby_playerID_lgID_orderedby_all.vue'
      
      import getAwardsPlayersPlayersFilteredbyFirstnameMiddlenameGroupedbyPlayerid from '../components/get_awards_players_players_filteredby_firstName_middleName_groupedby_playerID.vue'
      
      import getPlayersAwardsPlayersGroupedbyHscityPlayeridYearOrderedbyAll from '../components/get_players_awards_players_groupedby_hsCity_playerID_year_orderedby_all.vue'
      
      import getAwardsPlayersPlayersFilteredbyHeight from '../components/get_awards_players_players_filteredby_height.vue'
      
export default {
  components: {
    
      getPlayersAwardsPlayersFilteredbyPlayeridGroupedbyAll,
      
      getAwardsPlayersPlayersGroupedbyBirthcityPlayeridFirstnameBirthcountryMiddlenameOrderedbyAll,
      
      getPlayersAwardsPlayersGroupedbyAll,
      
      getAwardsPlayersPlayersFilteredbyYear,
      
      getPlayersAwardsPlayersGroupedbyPlayerid,
      
      getPlayersAwardsPlayersGroupedbyPlayeridLgidOrderedbyAll,
      
      getAwardsPlayersPlayersFilteredbyFirstnameMiddlenameGroupedbyPlayerid,
      
      getPlayersAwardsPlayersGroupedbyHscityPlayeridYearOrderedbyAll,
      
      getAwardsPlayersPlayersFilteredbyHeight,
      
  },
};
</script>
    