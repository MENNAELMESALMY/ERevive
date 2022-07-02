
<template>
  <div class="sideBar">
    <div class="header">
      <h4>Learning Management System</h4>
    </div>
  
    <ul class="clutsers">
      <li v-for="(card, i) in clustersNames" :key="i" class="cluster">
        <div class="clusterName" :title="card" :id="'clustersID' + i" @click="openClusterQueries('clustersID' + i,'queriesID' + i)">
           {{ card.substring(0, 19) + "..." }}
        </div>
        <ul class="queries" :id="'queriesID' + i">
          <li v-for="(item, j) in clusters[i]" :key="j" class="query">
            <router-link :to="'/App/' + card + '/' + item">
              <span class="queryName" :title="item">{{ item.substring(0, 19) + "..."}}</span>
            </router-link>
          </li>
        </ul>
      </li>
    </ul>
    <div class="footer">
      <h5>ERevive 2022</h5>
    </div>
  </div>
</template>

<script>
export default{
    data() {
        return {

        clustersNames: ['players_awards_players', 'awards_players', 'players', 'coaches', 'teams', 'players_awards_coaches', 'players_teams_teams', 'awards_coaches', 'players_coaches', 'awards_coaches_coaches_players', 'awards_coaches_series_post', 'awards_coaches_series_post_coaches', 'series_post_coaches', 'coaches_awards_coaches', 'awards_players_player_allstar', 'awards_players_teams', 'players_teams'],
        clusters: [['get_players_awards_players_filteredby_playerID_groupedby_all', 'get_awards_players_players_groupedby_birthCity_playerID_firstName_birthCountry_middleName_orderedby_all', 'get_players_awards_players_groupedby_all', 'get_awards_players_players_filteredby_year', 'get_players_awards_players_groupedby_playerID', 'get_players_awards_players_groupedby_playerID_lgID_orderedby_all', 'get_awards_players_players_filteredby_firstName_middleName_groupedby_playerID', 'get_players_awards_players_groupedby_hsCity_playerID_year_orderedby_all', 'get_awards_players_players_filteredby_height'], ['get_awards_players_filteredby_year_groupedby_all', 'get_awards_players_groupedby_all', 'get_awards_players_groupedby_playerID_lgID', 'get_awards_players_filteredby_lgID_year_groupedby_year', 'get_awards_players_groupedby_playerID_orderedby_all', 'get_awards_players_orderedby_all'], ['get_players_filteredby_playerID_groupedby_all', 'get_players_filteredby_height_groupedby_all', 'get_players_filteredby_weight_groupedby_all', 'get_players_groupedby_all'], ['get_coaches_filteredby_coachID_groupedby_all', 'get_coaches_groupedby_all', 'get_coaches_filteredby_year_groupedby_coachID_year', 'get_coaches_groupedby_tmID_coachID_orderedby_all', 'get_coaches_groupedby_coachID_orderedby_all', 'get_coaches_groupedby_year_orderedby_all', 'get_coaches_filteredby_year', 'get_coaches_orderedby_all'], ['get_teams'], ['get_players_awards_coaches_groupedby_id_firstName_middleName_orderedby_all', 'get_players_awards_coaches', 'get_players_awards_coaches_filteredby_id', 'get_players_awards_coaches_groupedby_id_firstName_middleName'], ['get_players_teams_teams_filteredby_id_groupedby_all', 'get_players_teams_teams_groupedby_name_lgID', 'get_players_teams_teams_filteredby_name'], ['get_awards_coaches', 'get_awards_coaches_filteredby_coachID_id'], ['get_players_coaches_groupedby_playerID', 'get_players_coaches_groupedby_coachID_playerID_orderedby_all', 'get_players_coaches', 'get_players_coaches_groupedby_playerID_orderedby_all'], ['get_awards_coaches_coaches_players', 'get_awards_coaches_coaches_players_filteredby_year', 'get_awards_coaches_coaches_players_filteredby_playerID'], ['get_awards_coaches_series_post_groupedby_all_orderedby_all', 'get_awards_coaches_series_post', 'get_awards_coaches_series_post_groupedby_coachID_id_orderedby_all', 'get_awards_coaches_series_post_groupedby_id', 'get_awards_coaches_series_post_groupedby_id_orderedby_all'], ['get_awards_coaches_series_post_coaches_filteredby_id', 'get_awards_coaches_series_post_coaches'], ['get_series_post_coaches'], ['get_coaches_awards_coaches_filteredby_year', 'get_awards_coaches_coaches_groupedby_coachID', 'get_awards_coaches_coaches_orderedby_all'], ['get_awards_players_player_allstar_groupedby_minutes', 'get_awards_players_player_allstar_orderedby_minutes'], ['get_awards_players_teams_filteredby_name_groupedby_name', 'get_awards_players_teams_groupedby_playerID', 'get_awards_players_teams', 'get_awards_players_teams_filteredby_name_year', 'get_awards_players_teams_filteredby_year'], ['get_players_teams_filteredby_name_year', 'get_players_teams_filteredby_name_groupedby_name_playerID_year', 'get_players_teams_filteredby_year_groupedby_firstName_year_middleName', 'get_players_teams_groupedby_playerID', 'get_players_teams_groupedby_year', 'get_players_teams']],
        
        };
    },
    methods: {
    openClusterQueries(clusterid,queryid) {
      if (document.getElementById(queryid).style.display == "none"){
        document.getElementById(queryid).style.display = "block";
        document.getElementById(clusterid).style.backgroundColor = "rgba(200,206,206,0.1)";
        document.getElementById(clusterid).onmouseover = function() {
          document.getElementById(clusterid).style.backgroundColor = "rgba(200,206,206,0.1)";
        }
        document.getElementById(clusterid).onmouseout = function() {
          document.getElementById(clusterid).style.backgroundColor = "rgba(200,206,206,0.1)";
        }
      }else{
        document.getElementById(queryid).style.display = "none";
        document.getElementById(clusterid).style.backgroundColor = "#0f1136";
        document.getElementById(clusterid).onmouseover = function() {
          document.getElementById(clusterid).style.backgroundColor = "rgba(200,206,206,0.1)";
        }
        document.getElementById(clusterid).onmouseout = function() {
          document.getElementById(clusterid).style.backgroundColor = "#0f1136";
        }
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.sideBar {
  color: white;
  background-color: #0f1136;
  float: left;
  width: 230px;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  bottom: 0;
  padding: 0.5em;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  overflow-x: hidden;
  scrollbar-width: thin;
  scrollbar-color: #0f1136 #0f1136;
  &::-webkit-scrollbar {
    width: 1px;
  }
  &::-webkit-scrollbar-track {
    background-color: #0f1136;
  }
  &::-webkit-scrollbar-thumb {
    background-color: #0f1136;
  }
}
.header,
.footer {
  text-align: center;
  font-weight: 700;
}
.clutsers,
.queries {
  margin: 0;
  padding: 0;
}
.clutsers {
  padding-top: 20px;
}
.queries {
  margin-top: 15px;
  margin-bottom: 15px;
  display: none;
  transition: all 0.4s ease;
}
.cluster,
.query {
  margin: 0;
  padding: 0;
  padding-left: 5px;
  list-style: none;
  padding-top: 5px;
  padding-bottom: 10px;
  a {
    color: white;
    text-decoration: none;
    padding-left: 10px;
  }
}
.clusterName {
  font-size: 16px;
  font-weight: 700;
  color: white;
  padding-top: 15px;
  padding-bottom: 15px;
  padding-left: 5px;
  padding-right: 5px;
  width: 90%;
  cursor: pointer;
  &:hover {
    background-color: rgb(200, 206, 206, 0.1);
    border-radius: 7px;
  }
}
.query {
  padding-top: 12px;
  width: 90%;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  &:hover {
    background-color: rgb(200, 206, 206, 0.1);
  }
}
</style>
  