<template>
    <div class="dashboard">
        <div>		<label>awards_coaches_id</label>
		<input type="text" v-model="awards_coaches_id">
		<label> equal to</label>

        <input type="submit"
        value="Call endpoint"
        @click='call_request'>
        </div>
        <table>
        <tr>
		<th>awards coaches id</th>
		<th>awards coaches coachID</th>
		<th>awards coaches award</th>
		<th>awards coaches lgID</th>
		<th>awards coaches note</th>
		<th>series post id</th>
		<th>series post year</th>
		<th>series post round</th>
		<th>series post series</th>
		<th>series post tmIDWinner</th>
		<th>series post lgIDWinner</th>
		<th>series post tmIDLoser</th>
		<th>series post lgIDLoser</th>
		<th>series post w</th>
		<th>series post L</th>
		<th>coaches coachID</th>
		<th>coaches year</th>
		<th>coaches tmID</th>
		<th>coaches lgID</th>
		<th>coaches stint</th>
		<th>coaches won</th>
		<th>coaches lost</th>
		<th>coaches post wins</th>
		<th>coaches post losses</th>
		</tr><tr v-for='(row,i) in dashboard_data' :key='i'>
			<td>{{row.awards_coaches_id}}</td>
			<td>{{row.awards_coaches_coachID}}</td>
			<td>{{row.awards_coaches_award}}</td>
			<td>{{row.awards_coaches_lgID}}</td>
			<td>{{row.awards_coaches_note}}</td>
			<td>{{row.series_post_id}}</td>
			<td>{{row.series_post_year}}</td>
			<td>{{row.series_post_round}}</td>
			<td>{{row.series_post_series}}</td>
			<td>{{row.series_post_tmIDWinner}}</td>
			<td>{{row.series_post_lgIDWinner}}</td>
			<td>{{row.series_post_tmIDLoser}}</td>
			<td>{{row.series_post_lgIDLoser}}</td>
			<td>{{row.series_post_w}}</td>
			<td>{{row.series_post_L}}</td>
			<td>{{row.coaches_coachID}}</td>
			<td>{{row.coaches_year}}</td>
			<td>{{row.coaches_tmID}}</td>
			<td>{{row.coaches_lgID}}</td>
			<td>{{row.coaches_stint}}</td>
			<td>{{row.coaches_won}}</td>
			<td>{{row.coaches_lost}}</td>
			<td>{{row.coaches_post_wins}}</td>
			<td>{{row.coaches_post_losses}}</td>
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
    dashboard_data: state => state.awards_coaches_series_post_coaches.get_awards_coaches_series_post_coaches_filteredby_id,
}),},
    methods: {
    call_request() {
    this.$store.dispatch("awards_coaches_series_post_coaches/get_awards_coaches_series_post_coaches_filteredby_id",
		 {'awards_coaches.id': this.awards_coaches_id,
		
      });
    }
    }
    };
</script>
    