
<template>
    <div>
    
      <get-players-teams-teams-filteredby-id-groupedby-all/>
      
      <get-players-teams-teams-groupedby-name-lgID/>
      
      <get-players-teams-teams-filteredby-name/>
      
    </div>
</template>

    <style lang="scss" scoped>
    .home {
    padding: 30px;
    }
    </style>

    <script>
    
      import getPlayersTeamsTeamsFilteredbyIdGroupedbyAll from '../components/get_players_teams_teams_filteredby_id_groupedby_all.vue'
      
      import getPlayersTeamsTeamsGroupedbyNameLgid from '../components/get_players_teams_teams_groupedby_name_lgID.vue'
      
      import getPlayersTeamsTeamsFilteredbyName from '../components/get_players_teams_teams_filteredby_name.vue'
      
export default {
  components: {
    
      getPlayersTeamsTeamsFilteredbyIdGroupedbyAll,
      
      getPlayersTeamsTeamsGroupedbyNameLgid,
      
      getPlayersTeamsTeamsFilteredbyName,
      
  },
};
</script>
    