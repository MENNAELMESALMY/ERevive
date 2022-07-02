<template>
    <div class="dashboard">
        <div class="sidebar">		<p>Filters</p>
		<div class="filters">
		<div>
		<label> greater than or equal to</label>
		<label>players_playerID</label>
		</div>
		<div>
		<input type="text" v-model="players_playerID">
		</div>
		</div>

        <input type="submit"
        value="Call endpoint"
        class="button"
        @click='call_request'>
        </div>

        <div class="table_nav">
        <h2>players_awards_players</h2>
    </div>
    <div>
        <table class="dashboard_table">
        <tr>
		<th>players playerID</th>
		<th>players useFirst</th>
		<th>players firstName</th>
		<th>players middleName</th>
		<th>players lastName</th>
		<th>players nameGiven</th>
		<th>players fullGivenName</th>
		<th>players nameSuffix</th>
		<th>players nameNick</th>
		<th>players pos</th>
		<th>players firstseason</th>
		<th>players lastseason</th>
		<th>players height</th>
		<th>players weight</th>
		<th>players college</th>
		<th>players collegeOther</th>
		<th>players birthDate</th>
		<th>players birthCity</th>
		<th>players birthState</th>
		<th>players birthCountry</th>
		<th>players highSchool</th>
		<th>players hsCity</th>
		<th>players hsState</th>
		<th>players hsCountry</th>
		<th>players deathDate</th>
		<th>players race</th>
		<th>awards players playerID</th>
		<th>awards players award</th>
		<th>awards players year</th>
		<th>awards players lgID</th>
		<th>awards players note</th>
		<th>awards players pos</th>
		<th>avg players height</th>
		<th>count all</th>
		</tr><tr v-for='(row,i) in dashboard_data' :key='i' class='data_rows'>
			<td>{{row.players_playerID}}</td>
			<td>{{row.players_useFirst}}</td>
			<td>{{row.players_firstName}}</td>
			<td>{{row.players_middleName}}</td>
			<td>{{row.players_lastName}}</td>
			<td>{{row.players_nameGiven}}</td>
			<td>{{row.players_fullGivenName}}</td>
			<td>{{row.players_nameSuffix}}</td>
			<td>{{row.players_nameNick}}</td>
			<td>{{row.players_pos}}</td>
			<td>{{row.players_firstseason}}</td>
			<td>{{row.players_lastseason}}</td>
			<td>{{row.players_height}}</td>
			<td>{{row.players_weight}}</td>
			<td>{{row.players_college}}</td>
			<td>{{row.players_collegeOther}}</td>
			<td>{{row.players_birthDate}}</td>
			<td>{{row.players_birthCity}}</td>
			<td>{{row.players_birthState}}</td>
			<td>{{row.players_birthCountry}}</td>
			<td>{{row.players_highSchool}}</td>
			<td>{{row.players_hsCity}}</td>
			<td>{{row.players_hsState}}</td>
			<td>{{row.players_hsCountry}}</td>
			<td>{{row.players_deathDate}}</td>
			<td>{{row.players_race}}</td>
			<td>{{row.awards_players_playerID}}</td>
			<td>{{row.awards_players_award}}</td>
			<td>{{row.awards_players_year}}</td>
			<td>{{row.awards_players_lgID}}</td>
			<td>{{row.awards_players_note}}</td>
			<td>{{row.awards_players_pos}}</td>
			<td>{{row.avg_players_height}}</td>
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
		players_playerID:"",

    };
    },
    computed: {
    ...mapState({
    dashboard_data: state => state.players_awards_players.get_players_awards_players_filteredby_playerID_groupedby_all,
}),},
    methods: {
    call_request() {
    this.$store.dispatch("players_awards_players/get_players_awards_players_filteredby_playerID_groupedby_all",
		 {'players.playerID': this.players_playerID,
		
      });
    }
    }
    };
</script>
    