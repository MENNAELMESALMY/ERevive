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
		<th>count all</th>
		</tr><tr v-for='(row,i) in dashboard_data' :key='i'>
			<td>{{row.awards_players_playerID}}</td>
			<td>{{row.awards_players_award}}</td>
			<td>{{row.awards_players_year}}</td>
			<td>{{row.awards_players_lgID}}</td>
			<td>{{row.awards_players_note}}</td>
			<td>{{row.awards_players_pos}}</td>
			<td>{{row.count_all}}</td>
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
    dashboard_data: state => state.awards_players.get_awards_players_filteredby_year_groupedby_all,
}),},
    methods: {
    call_request() {
    this.$store.dispatch("awards_players/get_awards_players_filteredby_year_groupedby_all",
		 {'awards_players.year': this.awards_players_year,
		
      });
    }
    }
    };
</script>
    