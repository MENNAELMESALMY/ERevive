<template>
    <div class="dashboard">
        <div class="sidebar">		<p>Filters</p>
		<div class="filters">
		</div>

        <input type="submit"
        value="Call endpoint"
        class="button"
        @click='call_request'>
        </div>

        <div class="table_nav">
        <h2>players</h2>
        <div class="buttons">
            <router-link to="" class="button">Add +</router-link>
            <router-link to="" class="button">edit</router-link>
            <button class="button" @click='delete_entity'>delete</button>
		</div>
        
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
		<th>max players height</th>
		<th>avg players hsCity</th>
		<th>min players playerID</th>
		<th>max players birthDate</th>
		<th>count all</th>
		<th>avg players weight</th>
		<th>max players hsCity</th>
		<th>min players weight</th>
		<th>avg players playerID</th>
		<th>avg players height</th>
		<th>min players birthDate</th>
		<th>min players hsCity</th>
		<th>max players playerID</th>
		<th>max players weight</th>
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
			<td>{{row.max_players_height}}</td>
			<td>{{row.avg_players_hsCity}}</td>
			<td>{{row.min_players_playerID}}</td>
			<td>{{row.max_players_birthDate}}</td>
			<td>{{row.count_all}}</td>
			<td>{{row.avg_players_weight}}</td>
			<td>{{row.max_players_hsCity}}</td>
			<td>{{row.min_players_weight}}</td>
			<td>{{row.avg_players_playerID}}</td>
			<td>{{row.avg_players_height}}</td>
			<td>{{row.min_players_birthDate}}</td>
			<td>{{row.min_players_hsCity}}</td>
			<td>{{row.max_players_playerID}}</td>
			<td>{{row.max_players_weight}}</td>
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

    };
    },
    computed: {
    ...mapState({
    dashboard_data: state => state.players.get_players_groupedby_all,
}),},
    methods: {
    call_request() {
    this.$store.dispatch("players/get_players_groupedby_all",
		 {
      });
    }
    }
    };
</script>
    