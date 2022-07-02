<template>
    <div class="dashboard">
        <div class="sidebar">		<p>Filters</p>
		<div class="filters">
		<div>
		<label> equal to</label>
		<label>players_teams_id</label>
		</div>
		<div>
		<input type="number" v-model="players_teams_id">
		</div>
		</div>

        <input type="submit"
        value="Call endpoint"
        class="button"
        @click='call_request'>
        </div>

        <div class="table_nav">
        <h2>players_teams_teams</h2>
    </div>
    <div>
        <table class="dashboard_table">
        <tr>
		<th>players teams id</th>
		<th>players teams playerID</th>
		<th>players teams year</th>
		<th>players teams stint</th>
		<th>players teams tmID</th>
		<th>players teams lgID</th>
		<th>players teams GP</th>
		<th>players teams GS</th>
		<th>players teams minutes</th>
		<th>players teams points</th>
		<th>players teams oRebounds</th>
		<th>players teams dRebounds</th>
		<th>players teams rebounds</th>
		<th>players teams assists</th>
		<th>players teams steals</th>
		<th>players teams blocks</th>
		<th>players teams turnovers</th>
		<th>players teams PF</th>
		<th>players teams fgAttempted</th>
		<th>players teams fgMade</th>
		<th>players teams ftAttempted</th>
		<th>players teams ftMade</th>
		<th>players teams threeAttempted</th>
		<th>players teams threeMade</th>
		<th>players teams PostGP</th>
		<th>players teams PostGS</th>
		<th>players teams PostMinutes</th>
		<th>players teams PostPoints</th>
		<th>players teams PostoRebounds</th>
		<th>players teams PostdRebounds</th>
		<th>players teams PostRebounds</th>
		<th>players teams PostAssists</th>
		<th>players teams PostSteals</th>
		<th>players teams PostBlocks</th>
		<th>players teams PostTurnovers</th>
		<th>players teams PostPF</th>
		<th>players teams PostfgAttempted</th>
		<th>players teams PostfgMade</th>
		<th>players teams PostftAttempted</th>
		<th>players teams PostftMade</th>
		<th>players teams PostthreeAttempted</th>
		<th>players teams PostthreeMade</th>
		<th>players teams note</th>
		<th>teams year</th>
		<th>teams lgID</th>
		<th>teams tmID</th>
		<th>teams franchID</th>
		<th>teams confID</th>
		<th>teams divID</th>
		<th>teams rank</th>
		<th>teams confRank</th>
		<th>teams playoff</th>
		<th>teams name</th>
		<th>count all</th>
		</tr><tr v-for='(row,i) in dashboard_data' :key='i' class='data_rows'>
			<td>{{row.players_teams_id}}</td>
			<td>{{row.players_teams_playerID}}</td>
			<td>{{row.players_teams_year}}</td>
			<td>{{row.players_teams_stint}}</td>
			<td>{{row.players_teams_tmID}}</td>
			<td>{{row.players_teams_lgID}}</td>
			<td>{{row.players_teams_GP}}</td>
			<td>{{row.players_teams_GS}}</td>
			<td>{{row.players_teams_minutes}}</td>
			<td>{{row.players_teams_points}}</td>
			<td>{{row.players_teams_oRebounds}}</td>
			<td>{{row.players_teams_dRebounds}}</td>
			<td>{{row.players_teams_rebounds}}</td>
			<td>{{row.players_teams_assists}}</td>
			<td>{{row.players_teams_steals}}</td>
			<td>{{row.players_teams_blocks}}</td>
			<td>{{row.players_teams_turnovers}}</td>
			<td>{{row.players_teams_PF}}</td>
			<td>{{row.players_teams_fgAttempted}}</td>
			<td>{{row.players_teams_fgMade}}</td>
			<td>{{row.players_teams_ftAttempted}}</td>
			<td>{{row.players_teams_ftMade}}</td>
			<td>{{row.players_teams_threeAttempted}}</td>
			<td>{{row.players_teams_threeMade}}</td>
			<td>{{row.players_teams_PostGP}}</td>
			<td>{{row.players_teams_PostGS}}</td>
			<td>{{row.players_teams_PostMinutes}}</td>
			<td>{{row.players_teams_PostPoints}}</td>
			<td>{{row.players_teams_PostoRebounds}}</td>
			<td>{{row.players_teams_PostdRebounds}}</td>
			<td>{{row.players_teams_PostRebounds}}</td>
			<td>{{row.players_teams_PostAssists}}</td>
			<td>{{row.players_teams_PostSteals}}</td>
			<td>{{row.players_teams_PostBlocks}}</td>
			<td>{{row.players_teams_PostTurnovers}}</td>
			<td>{{row.players_teams_PostPF}}</td>
			<td>{{row.players_teams_PostfgAttempted}}</td>
			<td>{{row.players_teams_PostfgMade}}</td>
			<td>{{row.players_teams_PostftAttempted}}</td>
			<td>{{row.players_teams_PostftMade}}</td>
			<td>{{row.players_teams_PostthreeAttempted}}</td>
			<td>{{row.players_teams_PostthreeMade}}</td>
			<td>{{row.players_teams_note}}</td>
			<td>{{row.teams_year}}</td>
			<td>{{row.teams_lgID}}</td>
			<td>{{row.teams_tmID}}</td>
			<td>{{row.teams_franchID}}</td>
			<td>{{row.teams_confID}}</td>
			<td>{{row.teams_divID}}</td>
			<td>{{row.teams_rank}}</td>
			<td>{{row.teams_confRank}}</td>
			<td>{{row.teams_playoff}}</td>
			<td>{{row.teams_name}}</td>
			<td>{{row.count_all}}</td>
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
		players_teams_id:"",

    };
    },
    computed: {
    ...mapState({
    dashboard_data: state => state.players_teams_teams.get_players_teams_teams_filteredby_id_groupedby_all,
}),},
    methods: {
    call_request() {
    this.$store.dispatch("players_teams_teams/get_players_teams_teams_filteredby_id_groupedby_all",
		 {'players_teams.id': this.players_teams_id,
		
      });
    }
    }
    };
</script>
    