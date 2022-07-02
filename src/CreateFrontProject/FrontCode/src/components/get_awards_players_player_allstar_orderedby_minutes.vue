<template>
    <div class="dashboard">
        <div class="sidebar">		<p>Filters</p>
		<div class="filters">
		<div>
		<label> sum</label><br>
		<label> equal to</label>
		<label>is_order_of_sum_minutes_desc</label>
		</div>
		<div>
		<input type="checkbox" v-model="is_order_of_sum_minutes_desc">
		</div>
		</div>

        <input type="submit"
        value="Call endpoint"
        class="button"
        @click='call_request'>
        </div>

        <div class="table_nav">
        <h2>awards_players_player_allstar</h2>
    </div>
    <div>
        <table class="dashboard_table">
        <tr>
		<th>awards players playerID</th>
		<th>awards players award</th>
		<th>awards players year</th>
		<th>awards players lgID</th>
		<th>awards players note</th>
		<th>awards players pos</th>
		<th>player allstar playerID</th>
		<th>player allstar last name</th>
		<th>player allstar first name</th>
		<th>player allstar season id</th>
		<th>player allstar conference</th>
		<th>player allstar league id</th>
		<th>player allstar games played</th>
		<th>player allstar minutes</th>
		<th>player allstar points</th>
		<th>player allstar o rebounds</th>
		<th>player allstar d rebounds</th>
		<th>player allstar rebounds</th>
		<th>player allstar assists</th>
		<th>player allstar steals</th>
		<th>player allstar blocks</th>
		<th>player allstar turnovers</th>
		<th>player allstar personal fouls</th>
		<th>player allstar fg attempted</th>
		<th>player allstar fg made</th>
		<th>player allstar ft attempted</th>
		<th>player allstar ft made</th>
		<th>player allstar three attempted</th>
		<th>player allstar three made</th>
		</tr><tr v-for='(row,i) in dashboard_data' :key='i' class='data_rows'>
			<td>{{row.awards_players_playerID}}</td>
			<td>{{row.awards_players_award}}</td>
			<td>{{row.awards_players_year}}</td>
			<td>{{row.awards_players_lgID}}</td>
			<td>{{row.awards_players_note}}</td>
			<td>{{row.awards_players_pos}}</td>
			<td>{{row.player_allstar_playerID}}</td>
			<td>{{row.player_allstar_last_name}}</td>
			<td>{{row.player_allstar_first_name}}</td>
			<td>{{row.player_allstar_season_id}}</td>
			<td>{{row.player_allstar_conference}}</td>
			<td>{{row.player_allstar_league_id}}</td>
			<td>{{row.player_allstar_games_played}}</td>
			<td>{{row.player_allstar_minutes}}</td>
			<td>{{row.player_allstar_points}}</td>
			<td>{{row.player_allstar_o_rebounds}}</td>
			<td>{{row.player_allstar_d_rebounds}}</td>
			<td>{{row.player_allstar_rebounds}}</td>
			<td>{{row.player_allstar_assists}}</td>
			<td>{{row.player_allstar_steals}}</td>
			<td>{{row.player_allstar_blocks}}</td>
			<td>{{row.player_allstar_turnovers}}</td>
			<td>{{row.player_allstar_personal_fouls}}</td>
			<td>{{row.player_allstar_fg_attempted}}</td>
			<td>{{row.player_allstar_fg_made}}</td>
			<td>{{row.player_allstar_ft_attempted}}</td>
			<td>{{row.player_allstar_ft_made}}</td>
			<td>{{row.player_allstar_three_attempted}}</td>
			<td>{{row.player_allstar_three_made}}</td>
		</tr>
        </table>
        </div>
    </div>
</template>

<style lang="scss" scoped>
@import "../scss/dashboard.scss";
</style>

<script>
    import { mapState } from "vuex";
    export default {
    name: "dashBoard",
    props: {},
    data: function () {
    return {
		is_order_of_sum_minutes_desc:"",

    };
    },
    computed: {
    ...mapState({
    dashboard_data: state => state.awards_players_player_allstar.get_awards_players_player_allstar_orderedby_minutes,
}),},
    methods: {
    call_request() {
    this.$store.dispatch("awards_players_player_allstar/get_awards_players_player_allstar_orderedby_minutes",
		 {'is_order_of_sum_minutes_desc': this.is_order_of_sum_minutes_desc,
		
      });
    }
    }
    };
</script>
    