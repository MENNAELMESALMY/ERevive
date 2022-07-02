
<template>
    <div>
    
      <get-awards-players-teams-filteredby-name-groupedby-name/>
      
      <get-awards-players-teams-groupedby-playerID/>
      
      <get-awards-players-teams/>
      
      <get-awards-players-teams-filteredby-name-year/>
      
      <get-awards-players-teams-filteredby-year/>
      
    </div>
</template>

    <style lang="scss" scoped>
    .home {
    padding: 30px;
    }
    </style>

    <script>
    
      import getAwardsPlayersTeamsFilteredbyNameGroupedbyName from '../components/get_awards_players_teams_filteredby_name_groupedby_name.vue'
      
      import getAwardsPlayersTeamsGroupedbyPlayerid from '../components/get_awards_players_teams_groupedby_playerID.vue'
      
      import getAwardsPlayersTeams from '../components/get_awards_players_teams.vue'
      
      import getAwardsPlayersTeamsFilteredbyNameYear from '../components/get_awards_players_teams_filteredby_name_year.vue'
      
      import getAwardsPlayersTeamsFilteredbyYear from '../components/get_awards_players_teams_filteredby_year.vue'
      
export default {
  components: {
    
      getAwardsPlayersTeamsFilteredbyNameGroupedbyName,
      
      getAwardsPlayersTeamsGroupedbyPlayerid,
      
      getAwardsPlayersTeams,
      
      getAwardsPlayersTeamsFilteredbyNameYear,
      
      getAwardsPlayersTeamsFilteredbyYear,
      
  },
};
</script>
    