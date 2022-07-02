
<template>
    <div>
    
      <get-awards-players-player-allstar-groupedby-minutes/>
      
      <get-awards-players-player-allstar-orderedby-minutes/>
      
    </div>
</template>

    <style lang="scss" scoped>
    .home {
    padding: 30px;
    }
    </style>

    <script>
    
      import getAwardsPlayersPlayerAllstarGroupedbyMinutes from '../components/get_awards_players_player_allstar_groupedby_minutes.vue'
      
      import getAwardsPlayersPlayerAllstarOrderedbyMinutes from '../components/get_awards_players_player_allstar_orderedby_minutes.vue'
      
export default {
  components: {
    
      getAwardsPlayersPlayerAllstarGroupedbyMinutes,
      
      getAwardsPlayersPlayerAllstarOrderedbyMinutes,
      
  },
};
</script>
    