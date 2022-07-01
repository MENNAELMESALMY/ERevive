
<template>
    <div>
    
      <get-awards-coaches-coaches-players/>
      
      <get-awards-coaches-coaches-players-filteredby-year/>
      
      <get-awards-coaches-coaches-players-filteredby-playerID/>
      
    </div>
</template>

    <style lang="scss" scoped>
    .home {
    padding: 30px;
    }
    </style>

    <script>
    
      import getAwardsCoachesCoachesPlayers from '../components/get_awards_coaches_coaches_players.vue'
      
      import getAwardsCoachesCoachesPlayersFilteredbyYear from '../components/get_awards_coaches_coaches_players_filteredby_year.vue'
      
      import getAwardsCoachesCoachesPlayersFilteredbyPlayerid from '../components/get_awards_coaches_coaches_players_filteredby_playerID.vue'
      
export default {
  components: {
    
      getAwardsCoachesCoachesPlayers,
      
      getAwardsCoachesCoachesPlayersFilteredbyYear,
      
      getAwardsCoachesCoachesPlayersFilteredbyPlayerid,
      
  },
};
</script>
    