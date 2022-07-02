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
        <h2>teams</h2>
        <div class="buttons">
            <router-link to="" class="button">Add +</router-link>
            <router-link to="" class="button">edit</router-link>
            <button class="button" @click='delete_entity'>delete</button>
		</div>
        
    </div>
    <div>
        <table class="dashboard_table">
        <tr>
		<th>year</th>
		<th>lgID</th>
		<th>tmID</th>
		<th>franchID</th>
		<th>confID</th>
		<th>divID</th>
		<th>rank</th>
		<th>confRank</th>
		<th>playoff</th>
		<th>name</th>
		</tr><tr v-for='(row,i) in dashboard_data' :key='i' class='data_rows'>
			<td>{{row.year}}</td>
			<td>{{row.lgID}}</td>
			<td>{{row.tmID}}</td>
			<td>{{row.franchID}}</td>
			<td>{{row.confID}}</td>
			<td>{{row.divID}}</td>
			<td>{{row.rank}}</td>
			<td>{{row.confRank}}</td>
			<td>{{row.playoff}}</td>
			<td>{{row.name}}</td>
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
    dashboard_data: state => state.teams.get_teams,
}),},
    methods: {
    call_request() {
    this.$store.dispatch("teams/get_teams",
		 {
      });
    }
    }
    };
</script>
    