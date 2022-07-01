<template>
    <div class="dashboard">
        <div>		<label>awards_coaches_id</label>
		<input type="text" v-model="awards_coaches_id">
		<label> less than or equal to</label>

        <input type="submit"
        value="Call endpoint"
        @click='call_request'>
        </div>
        <table>
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
		<th>awards coaches id</th>
		<th>awards coaches coachID</th>
		<th>awards coaches award</th>
		<th>awards coaches lgID</th>
		<th>awards coaches note</th>
		</tr><tr v-for='(row,i) in dashboard_data' :key='i'>
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
			<td>{{row.awards_coaches_id}}</td>
			<td>{{row.awards_coaches_coachID}}</td>
			<td>{{row.awards_coaches_award}}</td>
			<td>{{row.awards_coaches_lgID}}</td>
			<td>{{row.awards_coaches_note}}</td>
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
		awards_coaches_id:"",

    };
    },
    computed: {
    ...mapState({
    dashboard_data: state => state.players_awards_coaches.get_players_awards_coaches_filteredby_id,
}),},
    methods: {
    call_request() {
    this.$store.dispatch("players_awards_coaches/get_players_awards_coaches_filteredby_id",
		 {'awards_coaches.id': this.awards_coaches_id,
		
      });
    }
    }
    };
</script>
    