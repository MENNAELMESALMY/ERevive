<template>
    <div class="dashboard">
        <div class="filters">		
		<label>is_order_of_sum_minutes_desc</label>
		<input type="checkbox" v-model="is_order_of_sum_minutes_desc">
		<label> equal to</label>
		<label> sum</label><br>

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
		<th>player allstar playerID</th>
		<th>player allstar last name</th>
		<th>player allstar first name</th>
		</tr><tr v-for='(row,i) in dashboard_data' :key='i'>
			<td>{{row.awards_players_playerID}}</td>
			<td>{{row.awards_players_award}}</td>
			<td>{{row.awards_players_year}}</td>
			<td>{{row.awards_players_lgID}}</td>
			<td>{{row.awards_players_note}}</td>
			<td>{{row.awards_players_pos}}</td>
			<td>{{row.player_allstar_playerID}}</td>
			<td>{{row.player_allstar_last_name}}</td>
			<td>{{row.player_allstar_first_name}}</td>
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
    