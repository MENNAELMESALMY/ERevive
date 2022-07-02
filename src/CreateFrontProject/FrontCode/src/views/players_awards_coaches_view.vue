
<template>
    <div>
    
      <get-players-awards-coaches-groupedby-id-firstName-middleName-orderedby-all/>
      
      <get-players-awards-coaches/>
      
      <get-players-awards-coaches-filteredby-id/>
      
      <get-players-awards-coaches-groupedby-id-firstName-middleName/>
      
    </div>
</template>

    <style lang="scss" scoped>
    .home {
    padding: 30px;
    }
    </style>

    <script>
    
      import getPlayersAwardsCoachesGroupedbyIdFirstnameMiddlenameOrderedbyAll from '../components/get_players_awards_coaches_groupedby_id_firstName_middleName_orderedby_all.vue'
      
      import getPlayersAwardsCoaches from '../components/get_players_awards_coaches.vue'
      
      import getPlayersAwardsCoachesFilteredbyId from '../components/get_players_awards_coaches_filteredby_id.vue'
      
      import getPlayersAwardsCoachesGroupedbyIdFirstnameMiddlename from '../components/get_players_awards_coaches_groupedby_id_firstName_middleName.vue'
      
export default {
  components: {
    
      getPlayersAwardsCoachesGroupedbyIdFirstnameMiddlenameOrderedbyAll,
      
      getPlayersAwardsCoaches,
      
      getPlayersAwardsCoachesFilteredbyId,
      
      getPlayersAwardsCoachesGroupedbyIdFirstnameMiddlename,
      
  },
};
</script>
    