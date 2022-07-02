<template>
    <div class="dashboard">
        <div class="sidebar">		<p>Filters</p>
		<div class="filters">
		<div>
		<label> count</label><br>
		<label> equal to</label>
		<label>is_order_of_count_of_rows_desc</label>
		</div>
		<div>
		<input type="checkbox" v-model="is_order_of_count_of_rows_desc">
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
		<th>players firstName</th>
		<th>players birthCountry</th>
		<th>players playerID</th>
		<th>players birthCity</th>
		<th>players middleName</th>
		</tr><tr v-for='(row,i) in dashboard_data' :key='i' class='data_rows'>
			<td>{{row.players_firstName}}</td>
			<td>{{row.players_birthCountry}}</td>
			<td>{{row.players_playerID}}</td>
			<td>{{row.players_birthCity}}</td>
			<td>{{row.players_middleName}}</td>
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
		is_order_of_count_of_rows_desc:"",

    };
    },
    computed: {
    ...mapState({
    dashboard_data: state => state.players_awards_players.get_awards_players_players_groupedby_birthCity_playerID_firstName_birthCountry_middleName_orderedby_all,
}),},
    methods: {
    call_request() {
    this.$store.dispatch("players_awards_players/get_awards_players_players_groupedby_birthCity_playerID_firstName_birthCountry_middleName_orderedby_all",
		 {'is_order_of_count_of_rows_desc': this.is_order_of_count_of_rows_desc,
		
      });
    }
    }
    };
</script>
    