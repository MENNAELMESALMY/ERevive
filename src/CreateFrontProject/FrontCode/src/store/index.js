
//import * as Vue from "vue";
import Vuex from "vuex";
import players_awards_players from "./modules/players_awards_players.js";
import awards_players from "./modules/awards_players.js";
import players from "./modules/players.js";
import coaches from "./modules/coaches.js";
import teams from "./modules/teams.js";
import players_awards_coaches from "./modules/players_awards_coaches.js";
import players_teams_teams from "./modules/players_teams_teams.js";
import awards_coaches from "./modules/awards_coaches.js";
import players_coaches from "./modules/players_coaches.js";
import awards_coaches_coaches_players from "./modules/awards_coaches_coaches_players.js";
import awards_coaches_series_post from "./modules/awards_coaches_series_post.js";
import awards_coaches_series_post_coaches from "./modules/awards_coaches_series_post_coaches.js";
import series_post_coaches from "./modules/series_post_coaches.js";
import coaches_awards_coaches from "./modules/coaches_awards_coaches.js";
import awards_players_player_allstar from "./modules/awards_players_player_allstar.js";
import awards_players_teams from "./modules/awards_players_teams.js";
import players_teams from "./modules/players_teams.js";


import color_pallete from "./modules/color_pallete.js";
//Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
	players_awards_players,
	awards_players,
	players,
	coaches,
	teams,
	players_awards_coaches,
	players_teams_teams,
	awards_coaches,
	players_coaches,
	awards_coaches_coaches_players,
	awards_coaches_series_post,
	awards_coaches_series_post_coaches,
	series_post_coaches,
	coaches_awards_coaches,
	awards_players_player_allstar,
	awards_players_teams,
	players_teams,

    color_pallete
  },
});