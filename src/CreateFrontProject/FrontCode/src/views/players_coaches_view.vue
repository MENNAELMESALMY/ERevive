
<template>
    <div>
    
      <get-players-coaches-groupedby-playerID/>
      
      <get-players-coaches-groupedby-coachID-playerID-orderedby-all/>
      
      <get-players-coaches/>
      
      <get-players-coaches-groupedby-playerID-orderedby-all/>
      
    </div>
</template>

    <style lang="scss" scoped>
    .home {
    padding: 30px;
    }
    </style>

    <script>
    
      import getPlayersCoachesGroupedbyPlayerid from '../components/get_players_coaches_groupedby_playerID.vue'
      
      import getPlayersCoachesGroupedbyCoachidPlayeridOrderedbyAll from '../components/get_players_coaches_groupedby_coachID_playerID_orderedby_all.vue'
      
      import getPlayersCoaches from '../components/get_players_coaches.vue'
      
      import getPlayersCoachesGroupedbyPlayeridOrderedbyAll from '../components/get_players_coaches_groupedby_playerID_orderedby_all.vue'
      
export default {
  components: {
    
      getPlayersCoachesGroupedbyPlayerid,
      
      getPlayersCoachesGroupedbyCoachidPlayeridOrderedbyAll,
      
      getPlayersCoaches,
      
      getPlayersCoachesGroupedbyPlayeridOrderedbyAll,
      
  },
};
</script>
    