
import { createWebHistory, createRouter } from "vue-router";
import home from "../views/home.vue";
import players from "../views/players_view.vue";
import players_coaches from "../views/players_coaches_view.vue";
import awards_coaches from "../views/awards_coaches_view.vue";
import awards_coaches_coaches_players from "../views/awards_coaches_coaches_players_view.vue";
import coaches_awards_coaches from "../views/coaches_awards_coaches_view.vue";
import awards_players from "../views/awards_players_view.vue";
import series_post_coaches from "../views/series_post_coaches_view.vue";
import awards_players_player_allstar from "../views/awards_players_player_allstar_view.vue";
import teams from "../views/teams_view.vue";
import awards_players_teams from "../views/awards_players_teams_view.vue";
import awards_coaches_series_post_coaches from "../views/awards_coaches_series_post_coaches_view.vue";
import players_awards_coaches from "../views/players_awards_coaches_view.vue";
import players_awards_players from "../views/players_awards_players_view.vue";
import awards_coaches_series_post from "../views/awards_coaches_series_post_view.vue";
import players_teams_teams from "../views/players_teams_teams_view.vue";
import players_teams from "../views/players_teams_view.vue";
import coaches from "../views/coaches_view.vue";
const routes = [
  {
    path: "/",
    name: "home",
    component: home,
  },

		{
		path: "/players_awards_players",
		name: "players_awards_players",
		component: players_awards_players
		},

		{
		path: "/awards_players",
		name: "awards_players",
		component: awards_players
		},

		{
		path: "/players",
		name: "players",
		component: players
		},

		{
		path: "/coaches",
		name: "coaches",
		component: coaches
		},

		{
		path: "/teams",
		name: "teams",
		component: teams
		},

		{
		path: "/players_awards_coaches",
		name: "players_awards_coaches",
		component: players_awards_coaches
		},

		{
		path: "/players_teams_teams",
		name: "players_teams_teams",
		component: players_teams_teams
		},

		{
		path: "/awards_coaches",
		name: "awards_coaches",
		component: awards_coaches
		},

		{
		path: "/players_coaches",
		name: "players_coaches",
		component: players_coaches
		},

		{
		path: "/awards_coaches_coaches_players",
		name: "awards_coaches_coaches_players",
		component: awards_coaches_coaches_players
		},

		{
		path: "/awards_coaches_series_post",
		name: "awards_coaches_series_post",
		component: awards_coaches_series_post
		},

		{
		path: "/awards_coaches_series_post_coaches",
		name: "awards_coaches_series_post_coaches",
		component: awards_coaches_series_post_coaches
		},

		{
		path: "/series_post_coaches",
		name: "series_post_coaches",
		component: series_post_coaches
		},

		{
		path: "/coaches_awards_coaches",
		name: "coaches_awards_coaches",
		component: coaches_awards_coaches
		},

		{
		path: "/awards_players_player_allstar",
		name: "awards_players_player_allstar",
		component: awards_players_player_allstar
		},

		{
		path: "/awards_players_teams",
		name: "awards_players_teams",
		component: awards_players_teams
		},

		{
		path: "/players_teams",
		name: "players_teams",
		component: players_teams
		},

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
    