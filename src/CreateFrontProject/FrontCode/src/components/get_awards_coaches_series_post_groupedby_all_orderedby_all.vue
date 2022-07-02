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
        <h2>awards_coaches_series_post</h2>
    </div>
    <div>
        <table class="dashboard_table">
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
		</tr><tr v-for='(row,i) in dashboard_data' :key='i' class='data_rows'>
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
    dashboard_data: state => state.awards_coaches_series_post.get_awards_coaches_series_post_groupedby_all_orderedby_all,
}),},
    methods: {
    call_request() {
    this.$store.dispatch("awards_coaches_series_post/get_awards_coaches_series_post_groupedby_all_orderedby_all",
		 {'is_order_of_count_of_rows_desc': this.is_order_of_count_of_rows_desc,
		
      });
    }
    }
    };
</script>
    