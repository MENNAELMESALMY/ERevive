
import { createWebHistory, createRouter } from "vue-router";
import home from "../views/home.vue";
import main_page from "../views/main_page.vue";
import get_awards_players_teams_groupedby_playerID from "../components/get_awards_players_teams_groupedby_playerID.vue";
import get_players_filteredby_height_groupedby_all from "../components/get_players_filteredby_height_groupedby_all.vue";
import get_players_awards_coaches_filteredby_id from "../components/get_players_awards_coaches_filteredby_id.vue";
import get_coaches_filteredby_year_groupedby_coachID_year from "../components/get_coaches_filteredby_year_groupedby_coachID_year.vue";
import get_awards_coaches_coaches_players_filteredby_year from "../components/get_awards_coaches_coaches_players_filteredby_year.vue";
import get_players_teams_teams_filteredby_id_groupedby_all from "../components/get_players_teams_teams_filteredby_id_groupedby_all.vue";
import get_awards_coaches_series_post_groupedby_all_orderedby_all from "../components/get_awards_coaches_series_post_groupedby_all_orderedby_all.vue";
import get_awards_players_player_allstar_groupedby_minutes from "../components/get_awards_players_player_allstar_groupedby_minutes.vue";
import get_players_awards_players_groupedby_all from "../components/get_players_awards_players_groupedby_all.vue";
import get_awards_players_groupedby_playerID_orderedby_all from "../components/get_awards_players_groupedby_playerID_orderedby_all.vue";
import get_coaches_filteredby_coachID_groupedby_all from "../components/get_coaches_filteredby_coachID_groupedby_all.vue";
import get_coaches_groupedby_tmID_coachID_orderedby_all from "../components/get_coaches_groupedby_tmID_coachID_orderedby_all.vue";
import get_awards_players_players_filteredby_year from "../components/get_awards_players_players_filteredby_year.vue";
import get_awards_coaches_coaches_groupedby_coachID from "../components/get_awards_coaches_coaches_groupedby_coachID.vue";
import get_players_teams_filteredby_name_groupedby_name_playerID_year from "../components/get_players_teams_filteredby_name_groupedby_name_playerID_year.vue";
import get_coaches_groupedby_all from "../components/get_coaches_groupedby_all.vue";
import get_coaches_groupedby_coachID_orderedby_all from "../components/get_coaches_groupedby_coachID_orderedby_all.vue";
import get_awards_players_groupedby_all from "../components/get_awards_players_groupedby_all.vue";
import get_players_awards_coaches_groupedby_id_firstName_middleName from "../components/get_players_awards_coaches_groupedby_id_firstName_middleName.vue";
import get_awards_coaches_series_post_groupedby_coachID_id_orderedby_all from "../components/get_awards_coaches_series_post_groupedby_coachID_id_orderedby_all.vue";
import get_players_teams_filteredby_name_year from "../components/get_players_teams_filteredby_name_year.vue";
import get_players_filteredby_playerID_groupedby_all from "../components/get_players_filteredby_playerID_groupedby_all.vue";
import get_awards_coaches_series_post_coaches_filteredby_id from "../components/get_awards_coaches_series_post_coaches_filteredby_id.vue";
import get_teams from "../components/get_teams.vue";
import get_players_teams_groupedby_playerID from "../components/get_players_teams_groupedby_playerID.vue";
import get_players_awards_players_groupedby_hsCity_playerID_year_orderedby_all from "../components/get_players_awards_players_groupedby_hsCity_playerID_year_orderedby_all.vue";
import get_coaches_filteredby_year from "../components/get_coaches_filteredby_year.vue";
import get_awards_players_teams_filteredby_name_year from "../components/get_awards_players_teams_filteredby_name_year.vue";
import get_players_coaches from "../components/get_players_coaches.vue";
import get_players_coaches_groupedby_playerID_orderedby_all from "../components/get_players_coaches_groupedby_playerID_orderedby_all.vue";
import get_awards_coaches_series_post_groupedby_id_orderedby_all from "../components/get_awards_coaches_series_post_groupedby_id_orderedby_all.vue";
import get_players_teams_teams_groupedby_name_lgID from "../components/get_players_teams_teams_groupedby_name_lgID.vue";
import get_players_filteredby_weight_groupedby_all from "../components/get_players_filteredby_weight_groupedby_all.vue";
import get_awards_players_players_groupedby_birthCity_playerID_firstName_birthCountry_middleName_orderedby_all from "../components/get_awards_players_players_groupedby_birthCity_playerID_firstName_birthCountry_middleName_orderedby_all.vue";
import get_coaches_groupedby_year_orderedby_all from "../components/get_coaches_groupedby_year_orderedby_all.vue";
import get_players_teams_filteredby_year_groupedby_firstName_year_middleName from "../components/get_players_teams_filteredby_year_groupedby_firstName_year_middleName.vue";
import get_players_awards_coaches_groupedby_id_firstName_middleName_orderedby_all from "../components/get_players_awards_coaches_groupedby_id_firstName_middleName_orderedby_all.vue";
import get_awards_players_groupedby_playerID_lgID from "../components/get_awards_players_groupedby_playerID_lgID.vue";
import get_players_teams_groupedby_year from "../components/get_players_teams_groupedby_year.vue";
import get_awards_players_players_filteredby_firstName_middleName_groupedby_playerID from "../components/get_awards_players_players_filteredby_firstName_middleName_groupedby_playerID.vue";
import get_awards_coaches_coaches_players from "../components/get_awards_coaches_coaches_players.vue";
import get_awards_coaches_coaches_players_filteredby_playerID from "../components/get_awards_coaches_coaches_players_filteredby_playerID.vue";
import get_awards_coaches_series_post_coaches from "../components/get_awards_coaches_series_post_coaches.vue";
import get_awards_players_teams from "../components/get_awards_players_teams.vue";
import get_players_awards_players_groupedby_playerID_lgID_orderedby_all from "../components/get_players_awards_players_groupedby_playerID_lgID_orderedby_all.vue";
import get_players_coaches_groupedby_playerID from "../components/get_players_coaches_groupedby_playerID.vue";
import get_awards_players_filteredby_year_groupedby_all from "../components/get_awards_players_filteredby_year_groupedby_all.vue";
import get_players_awards_players_groupedby_playerID from "../components/get_players_awards_players_groupedby_playerID.vue";
import get_awards_coaches_series_post_groupedby_id from "../components/get_awards_coaches_series_post_groupedby_id.vue";
import get_players_coaches_groupedby_coachID_playerID_orderedby_all from "../components/get_players_coaches_groupedby_coachID_playerID_orderedby_all.vue";
import get_awards_coaches_series_post from "../components/get_awards_coaches_series_post.vue";
import get_awards_players_filteredby_lgID_year_groupedby_year from "../components/get_awards_players_filteredby_lgID_year_groupedby_year.vue";
import get_awards_players_players_filteredby_height from "../components/get_awards_players_players_filteredby_height.vue";
import get_awards_players_orderedby_all from "../components/get_awards_players_orderedby_all.vue";
import get_awards_players_player_allstar_orderedby_minutes from "../components/get_awards_players_player_allstar_orderedby_minutes.vue";
import get_awards_players_teams_filteredby_year from "../components/get_awards_players_teams_filteredby_year.vue";
import get_coaches_orderedby_all from "../components/get_coaches_orderedby_all.vue";
import get_players_teams from "../components/get_players_teams.vue";
import get_awards_players_teams_filteredby_name_groupedby_name from "../components/get_awards_players_teams_filteredby_name_groupedby_name.vue";
import get_awards_coaches_coaches_orderedby_all from "../components/get_awards_coaches_coaches_orderedby_all.vue";
import get_players_awards_coaches from "../components/get_players_awards_coaches.vue";
import get_players_awards_players_filteredby_playerID_groupedby_all from "../components/get_players_awards_players_filteredby_playerID_groupedby_all.vue";
import get_coaches_awards_coaches_filteredby_year from "../components/get_coaches_awards_coaches_filteredby_year.vue";
import get_series_post_coaches from "../components/get_series_post_coaches.vue";
import get_awards_coaches_filteredby_coachID_id from "../components/get_awards_coaches_filteredby_coachID_id.vue";
import create_teams from "../components/create_teams.vue";
import get_players_groupedby_all from "../components/get_players_groupedby_all.vue";
import get_players_teams_teams_filteredby_name from "../components/get_players_teams_teams_filteredby_name.vue";
import get_awards_coaches from "../components/get_awards_coaches.vue";
const routes = [
  {
    path: "/",
    name: "home",
    component: home,
  },
  {
    path: "/App",
    name: "App",
    component: main_page,
    children:[
    
        {
        
        path: "players_awards_players/get_players_awards_players_filteredby_playerID_groupedby_all",
        name: "get_players_awards_players_filteredby_playerID_groupedby_all",
        component: get_players_awards_players_filteredby_playerID_groupedby_all,
        
        },
        
        {
        
        path: "players_awards_players/get_awards_players_players_groupedby_birthCity_playerID_firstName_birthCountry_middleName_orderedby_all",
        name: "get_awards_players_players_groupedby_birthCity_playerID_firstName_birthCountry_middleName_orderedby_all",
        component: get_awards_players_players_groupedby_birthCity_playerID_firstName_birthCountry_middleName_orderedby_all,
        
        },
        
        {
        
        path: "players_awards_players/get_players_awards_players_groupedby_all",
        name: "get_players_awards_players_groupedby_all",
        component: get_players_awards_players_groupedby_all,
        
        },
        
        {
        
        path: "players_awards_players/get_awards_players_players_filteredby_year",
        name: "get_awards_players_players_filteredby_year",
        component: get_awards_players_players_filteredby_year,
        
        },
        
        {
        
        path: "players_awards_players/get_players_awards_players_groupedby_playerID",
        name: "get_players_awards_players_groupedby_playerID",
        component: get_players_awards_players_groupedby_playerID,
        
        },
        
        {
        
        path: "players_awards_players/get_players_awards_players_groupedby_playerID_lgID_orderedby_all",
        name: "get_players_awards_players_groupedby_playerID_lgID_orderedby_all",
        component: get_players_awards_players_groupedby_playerID_lgID_orderedby_all,
        
        },
        
        {
        
        path: "players_awards_players/get_awards_players_players_filteredby_firstName_middleName_groupedby_playerID",
        name: "get_awards_players_players_filteredby_firstName_middleName_groupedby_playerID",
        component: get_awards_players_players_filteredby_firstName_middleName_groupedby_playerID,
        
        },
        
        {
        
        path: "players_awards_players/get_players_awards_players_groupedby_hsCity_playerID_year_orderedby_all",
        name: "get_players_awards_players_groupedby_hsCity_playerID_year_orderedby_all",
        component: get_players_awards_players_groupedby_hsCity_playerID_year_orderedby_all,
        
        },
        
        {
        
        path: "players_awards_players/get_awards_players_players_filteredby_height",
        name: "get_awards_players_players_filteredby_height",
        component: get_awards_players_players_filteredby_height,
        
        },
        
        {
        
        path: "awards_players/get_awards_players_filteredby_year_groupedby_all",
        name: "get_awards_players_filteredby_year_groupedby_all",
        component: get_awards_players_filteredby_year_groupedby_all,
        
        },
        
        {
        
        path: "awards_players/get_awards_players_groupedby_all",
        name: "get_awards_players_groupedby_all",
        component: get_awards_players_groupedby_all,
        
        },
        
        {
        
        path: "awards_players/get_awards_players_groupedby_playerID_lgID",
        name: "get_awards_players_groupedby_playerID_lgID",
        component: get_awards_players_groupedby_playerID_lgID,
        
        },
        
        {
        
        path: "awards_players/get_awards_players_filteredby_lgID_year_groupedby_year",
        name: "get_awards_players_filteredby_lgID_year_groupedby_year",
        component: get_awards_players_filteredby_lgID_year_groupedby_year,
        
        },
        
        {
        
        path: "awards_players/get_awards_players_groupedby_playerID_orderedby_all",
        name: "get_awards_players_groupedby_playerID_orderedby_all",
        component: get_awards_players_groupedby_playerID_orderedby_all,
        
        },
        
        {
        
        path: "awards_players/get_awards_players_orderedby_all",
        name: "get_awards_players_orderedby_all",
        component: get_awards_players_orderedby_all,
        
        },
        
        {
        
        path: "players/get_players_filteredby_playerID_groupedby_all",
        name: "get_players_filteredby_playerID_groupedby_all",
        component: get_players_filteredby_playerID_groupedby_all,
        
        },
        
        {
        
        path: "players/get_players_filteredby_height_groupedby_all",
        name: "get_players_filteredby_height_groupedby_all",
        component: get_players_filteredby_height_groupedby_all,
        
        },
        
        {
        
        path: "players/get_players_filteredby_weight_groupedby_all",
        name: "get_players_filteredby_weight_groupedby_all",
        component: get_players_filteredby_weight_groupedby_all,
        
        },
        
        {
        
        path: "players/get_players_groupedby_all",
        name: "get_players_groupedby_all",
        component: get_players_groupedby_all,
        
        },
        
        {
        
        path: "coaches/get_coaches_filteredby_coachID_groupedby_all",
        name: "get_coaches_filteredby_coachID_groupedby_all",
        component: get_coaches_filteredby_coachID_groupedby_all,
        
        },
        
        {
        
        path: "coaches/get_coaches_groupedby_all",
        name: "get_coaches_groupedby_all",
        component: get_coaches_groupedby_all,
        
        },
        
        {
        
        path: "coaches/get_coaches_filteredby_year_groupedby_coachID_year",
        name: "get_coaches_filteredby_year_groupedby_coachID_year",
        component: get_coaches_filteredby_year_groupedby_coachID_year,
        
        },
        
        {
        
        path: "coaches/get_coaches_groupedby_tmID_coachID_orderedby_all",
        name: "get_coaches_groupedby_tmID_coachID_orderedby_all",
        component: get_coaches_groupedby_tmID_coachID_orderedby_all,
        
        },
        
        {
        
        path: "coaches/get_coaches_groupedby_coachID_orderedby_all",
        name: "get_coaches_groupedby_coachID_orderedby_all",
        component: get_coaches_groupedby_coachID_orderedby_all,
        
        },
        
        {
        
        path: "coaches/get_coaches_groupedby_year_orderedby_all",
        name: "get_coaches_groupedby_year_orderedby_all",
        component: get_coaches_groupedby_year_orderedby_all,
        
        },
        
        {
        
        path: "coaches/get_coaches_filteredby_year",
        name: "get_coaches_filteredby_year",
        component: get_coaches_filteredby_year,
        
        },
        
        {
        
        path: "coaches/get_coaches_orderedby_all",
        name: "get_coaches_orderedby_all",
        component: get_coaches_orderedby_all,
        
        },
        
        {
        
        path: "teams/get_teams",
        name: "get_teams",
        component: get_teams,
        
        },
        
        {
        
        path: "teams/create_teams",
        name: "create_teams",
        component: create_teams,
        
        },
        
        {
        
        path: "players_awards_coaches/get_players_awards_coaches_groupedby_id_firstName_middleName_orderedby_all",
        name: "get_players_awards_coaches_groupedby_id_firstName_middleName_orderedby_all",
        component: get_players_awards_coaches_groupedby_id_firstName_middleName_orderedby_all,
        
        },
        
        {
        
        path: "players_awards_coaches/get_players_awards_coaches",
        name: "get_players_awards_coaches",
        component: get_players_awards_coaches,
        
        },
        
        {
        
        path: "players_awards_coaches/get_players_awards_coaches_filteredby_id",
        name: "get_players_awards_coaches_filteredby_id",
        component: get_players_awards_coaches_filteredby_id,
        
        },
        
        {
        
        path: "players_awards_coaches/get_players_awards_coaches_groupedby_id_firstName_middleName",
        name: "get_players_awards_coaches_groupedby_id_firstName_middleName",
        component: get_players_awards_coaches_groupedby_id_firstName_middleName,
        
        },
        
        {
        
        path: "players_teams_teams/get_players_teams_teams_filteredby_id_groupedby_all",
        name: "get_players_teams_teams_filteredby_id_groupedby_all",
        component: get_players_teams_teams_filteredby_id_groupedby_all,
        
        },
        
        {
        
        path: "players_teams_teams/get_players_teams_teams_groupedby_name_lgID",
        name: "get_players_teams_teams_groupedby_name_lgID",
        component: get_players_teams_teams_groupedby_name_lgID,
        
        },
        
        {
        
        path: "players_teams_teams/get_players_teams_teams_filteredby_name",
        name: "get_players_teams_teams_filteredby_name",
        component: get_players_teams_teams_filteredby_name,
        
        },
        
        {
        
        path: "awards_coaches/get_awards_coaches",
        name: "get_awards_coaches",
        component: get_awards_coaches,
        
        },
        
        {
        
        path: "awards_coaches/get_awards_coaches_filteredby_coachID_id",
        name: "get_awards_coaches_filteredby_coachID_id",
        component: get_awards_coaches_filteredby_coachID_id,
        
        },
        
        {
        
        path: "players_coaches/get_players_coaches_groupedby_playerID",
        name: "get_players_coaches_groupedby_playerID",
        component: get_players_coaches_groupedby_playerID,
        
        },
        
        {
        
        path: "players_coaches/get_players_coaches_groupedby_coachID_playerID_orderedby_all",
        name: "get_players_coaches_groupedby_coachID_playerID_orderedby_all",
        component: get_players_coaches_groupedby_coachID_playerID_orderedby_all,
        
        },
        
        {
        
        path: "players_coaches/get_players_coaches",
        name: "get_players_coaches",
        component: get_players_coaches,
        
        },
        
        {
        
        path: "players_coaches/get_players_coaches_groupedby_playerID_orderedby_all",
        name: "get_players_coaches_groupedby_playerID_orderedby_all",
        component: get_players_coaches_groupedby_playerID_orderedby_all,
        
        },
        
        {
        
        path: "awards_coaches_coaches_players/get_awards_coaches_coaches_players",
        name: "get_awards_coaches_coaches_players",
        component: get_awards_coaches_coaches_players,
        
        },
        
        {
        
        path: "awards_coaches_coaches_players/get_awards_coaches_coaches_players_filteredby_year",
        name: "get_awards_coaches_coaches_players_filteredby_year",
        component: get_awards_coaches_coaches_players_filteredby_year,
        
        },
        
        {
        
        path: "awards_coaches_coaches_players/get_awards_coaches_coaches_players_filteredby_playerID",
        name: "get_awards_coaches_coaches_players_filteredby_playerID",
        component: get_awards_coaches_coaches_players_filteredby_playerID,
        
        },
        
        {
        
        path: "awards_coaches_series_post/get_awards_coaches_series_post_groupedby_all_orderedby_all",
        name: "get_awards_coaches_series_post_groupedby_all_orderedby_all",
        component: get_awards_coaches_series_post_groupedby_all_orderedby_all,
        
        },
        
        {
        
        path: "awards_coaches_series_post/get_awards_coaches_series_post",
        name: "get_awards_coaches_series_post",
        component: get_awards_coaches_series_post,
        
        },
        
        {
        
        path: "awards_coaches_series_post/get_awards_coaches_series_post_groupedby_coachID_id_orderedby_all",
        name: "get_awards_coaches_series_post_groupedby_coachID_id_orderedby_all",
        component: get_awards_coaches_series_post_groupedby_coachID_id_orderedby_all,
        
        },
        
        {
        
        path: "awards_coaches_series_post/get_awards_coaches_series_post_groupedby_id",
        name: "get_awards_coaches_series_post_groupedby_id",
        component: get_awards_coaches_series_post_groupedby_id,
        
        },
        
        {
        
        path: "awards_coaches_series_post/get_awards_coaches_series_post_groupedby_id_orderedby_all",
        name: "get_awards_coaches_series_post_groupedby_id_orderedby_all",
        component: get_awards_coaches_series_post_groupedby_id_orderedby_all,
        
        },
        
        {
        
        path: "awards_coaches_series_post_coaches/get_awards_coaches_series_post_coaches_filteredby_id",
        name: "get_awards_coaches_series_post_coaches_filteredby_id",
        component: get_awards_coaches_series_post_coaches_filteredby_id,
        
        },
        
        {
        
        path: "awards_coaches_series_post_coaches/get_awards_coaches_series_post_coaches",
        name: "get_awards_coaches_series_post_coaches",
        component: get_awards_coaches_series_post_coaches,
        
        },
        
        {
        
        path: "series_post_coaches/get_series_post_coaches",
        name: "get_series_post_coaches",
        component: get_series_post_coaches,
        
        },
        
        {
        
        path: "coaches_awards_coaches/get_coaches_awards_coaches_filteredby_year",
        name: "get_coaches_awards_coaches_filteredby_year",
        component: get_coaches_awards_coaches_filteredby_year,
        
        },
        
        {
        
        path: "coaches_awards_coaches/get_awards_coaches_coaches_groupedby_coachID",
        name: "get_awards_coaches_coaches_groupedby_coachID",
        component: get_awards_coaches_coaches_groupedby_coachID,
        
        },
        
        {
        
        path: "coaches_awards_coaches/get_awards_coaches_coaches_orderedby_all",
        name: "get_awards_coaches_coaches_orderedby_all",
        component: get_awards_coaches_coaches_orderedby_all,
        
        },
        
        {
        
        path: "awards_players_player_allstar/get_awards_players_player_allstar_groupedby_minutes",
        name: "get_awards_players_player_allstar_groupedby_minutes",
        component: get_awards_players_player_allstar_groupedby_minutes,
        
        },
        
        {
        
        path: "awards_players_player_allstar/get_awards_players_player_allstar_orderedby_minutes",
        name: "get_awards_players_player_allstar_orderedby_minutes",
        component: get_awards_players_player_allstar_orderedby_minutes,
        
        },
        
        {
        
        path: "awards_players_teams/get_awards_players_teams_filteredby_name_groupedby_name",
        name: "get_awards_players_teams_filteredby_name_groupedby_name",
        component: get_awards_players_teams_filteredby_name_groupedby_name,
        
        },
        
        {
        
        path: "awards_players_teams/get_awards_players_teams_groupedby_playerID",
        name: "get_awards_players_teams_groupedby_playerID",
        component: get_awards_players_teams_groupedby_playerID,
        
        },
        
        {
        
        path: "awards_players_teams/get_awards_players_teams",
        name: "get_awards_players_teams",
        component: get_awards_players_teams,
        
        },
        
        {
        
        path: "awards_players_teams/get_awards_players_teams_filteredby_name_year",
        name: "get_awards_players_teams_filteredby_name_year",
        component: get_awards_players_teams_filteredby_name_year,
        
        },
        
        {
        
        path: "awards_players_teams/get_awards_players_teams_filteredby_year",
        name: "get_awards_players_teams_filteredby_year",
        component: get_awards_players_teams_filteredby_year,
        
        },
        
        {
        
        path: "players_teams/get_players_teams_filteredby_name_year",
        name: "get_players_teams_filteredby_name_year",
        component: get_players_teams_filteredby_name_year,
        
        },
        
        {
        
        path: "players_teams/get_players_teams_filteredby_name_groupedby_name_playerID_year",
        name: "get_players_teams_filteredby_name_groupedby_name_playerID_year",
        component: get_players_teams_filteredby_name_groupedby_name_playerID_year,
        
        },
        
        {
        
        path: "players_teams/get_players_teams_filteredby_year_groupedby_firstName_year_middleName",
        name: "get_players_teams_filteredby_year_groupedby_firstName_year_middleName",
        component: get_players_teams_filteredby_year_groupedby_firstName_year_middleName,
        
        },
        
        {
        
        path: "players_teams/get_players_teams_groupedby_playerID",
        name: "get_players_teams_groupedby_playerID",
        component: get_players_teams_groupedby_playerID,
        
        },
        
        {
        
        path: "players_teams/get_players_teams_groupedby_year",
        name: "get_players_teams_groupedby_year",
        component: get_players_teams_groupedby_year,
        
        },
        
        {
        
        path: "players_teams/get_players_teams",
        name: "get_players_teams",
        component: get_players_teams,
        
        },
        
    ]
  }
];
        
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
    