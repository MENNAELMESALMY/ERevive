<template>
    <div class="dashboard">
        <div>
        <input type="submit"
        value="Call endpoint"
        @click='call_request'>
        </div>
        <table>
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
		</tr><tr v-for='(row,i) in dashboard_data' :key='i'>
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
    