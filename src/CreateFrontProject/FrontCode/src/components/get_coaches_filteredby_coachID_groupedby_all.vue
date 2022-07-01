<template>
    <div class="dashboard">
        <div>		<label>coaches_coachID</label>
		<input type="text" v-model="coaches_coachID">
		<label> less than or equal to</label>

        <input type="submit"
        value="Call endpoint"
        @click='call_request'>
        </div>
        <table>
        <tr>
		<th>coaches coachID</th>
		<th>coaches year</th>
		<th>coaches tmID</th>
		<th>coaches lgID</th>
		<th>coaches stint</th>
		<th>coaches won</th>
		<th>coaches lost</th>
		<th>coaches post wins</th>
		<th>coaches post losses</th>
		<th>count all</th>
		</tr><tr v-for='(row,i) in dashboard_data' :key='i'>
			<td>{{row.coaches_coachID}}</td>
			<td>{{row.coaches_year}}</td>
			<td>{{row.coaches_tmID}}</td>
			<td>{{row.coaches_lgID}}</td>
			<td>{{row.coaches_stint}}</td>
			<td>{{row.coaches_won}}</td>
			<td>{{row.coaches_lost}}</td>
			<td>{{row.coaches_post_wins}}</td>
			<td>{{row.coaches_post_losses}}</td>
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
		coaches_coachID:"",

    };
    },
    computed: {
    ...mapState({
    dashboard_data: state => state.coaches.get_coaches_filteredby_coachID_groupedby_all,
}),},
    methods: {
    call_request() {
    this.$store.dispatch("coaches/get_coaches_filteredby_coachID_groupedby_all",
		 {'coaches.coachID': this.coaches_coachID,
		
      });
    }
    }
    };
</script>
    