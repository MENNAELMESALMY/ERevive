
<template>
    <div>
    
      <get-players-teams-filteredby-name-year/>
      
      <get-players-teams-filteredby-name-groupedby-name-playerID-year/>
      
      <get-players-teams-filteredby-year-groupedby-firstName-year-middleName/>
      
      <get-players-teams-groupedby-playerID/>
      
      <get-players-teams-groupedby-year/>
      
      <get-players-teams/>
      
    </div>
</template>

    <style lang="scss" scoped>
    .home {
    padding: 30px;
    }
    </style>

    <script>
    
      import getPlayersTeamsFilteredbyNameYear from '../components/get_players_teams_filteredby_name_year.vue'
      
      import getPlayersTeamsFilteredbyNameGroupedbyNamePlayeridYear from '../components/get_players_teams_filteredby_name_groupedby_name_playerID_year.vue'
      
      import getPlayersTeamsFilteredbyYearGroupedbyFirstnameYearMiddlename from '../components/get_players_teams_filteredby_year_groupedby_firstName_year_middleName.vue'
      
      import getPlayersTeamsGroupedbyPlayerid from '../components/get_players_teams_groupedby_playerID.vue'
      
      import getPlayersTeamsGroupedbyYear from '../components/get_players_teams_groupedby_year.vue'
      
      import getPlayersTeams from '../components/get_players_teams.vue'
      
export default {
  components: {
    
      getPlayersTeamsFilteredbyNameYear,
      
      getPlayersTeamsFilteredbyNameGroupedbyNamePlayeridYear,
      
      getPlayersTeamsFilteredbyYearGroupedbyFirstnameYearMiddlename,
      
      getPlayersTeamsGroupedbyPlayerid,
      
      getPlayersTeamsGroupedbyYear,
      
      getPlayersTeams,
      
  },
};
</script>
    