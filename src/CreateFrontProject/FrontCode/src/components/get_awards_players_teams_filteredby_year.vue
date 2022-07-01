<template>
    <div class="dashboard">
        <div>		<label>awards_players_year</label>
		<input type="number" v-model="awards_players_year">
		<label> equal to</label>

        <input type="submit"
        value="Call endpoint"
        @click='call_request'>
        </div>
        <table>
        <tr>
		<th>awards players playerID</th>
		<th>awards players award</th>
		<th>awards players year</th>
		<th>awards players lgID</th>
		<th>awards players note</th>
		<th>awards players pos</th>
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
		</tr><tr v-for='(row,i) in dashboard_data' :key='i'>
			<td>{{row.awards_players_playerID}}</td>
			<td>{{row.awards_players_award}}</td>
			<td>{{row.awards_players_year}}</td>
			<td>{{row.awards_players_lgID}}</td>
			<td>{{row.awards_players_note}}</td>
			<td>{{row.awards_players_pos}}</td>
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
		</tr>
        </table>
    </div>
</template>

<style lang="scss" scoped>
// @import "../scss/dashboard.scss";
</style>

<script>
    import { mapState } from "vuex";
    export default {
    name: "dashBoard",
    props: {},
    data: function () {
    return {
		awards_players_year:"",

    };
    },
    computed: {
    ...mapState({
    dashboard_data: state => state.awards_players_teams.get_awards_players_teams_filteredby_year,
}),},
    methods: {
    call_request() {
    this.$store.dispatch("awards_players_teams/get_awards_players_teams_filteredby_year",
		 {'awards_players.year': this.awards_players_year,
		
      });
    }
    }
    };
</script>
    