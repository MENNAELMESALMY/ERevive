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
        <h2>coaches</h2>
        <div class="buttons">
            <router-link to="" class="button">Add +</router-link>
            <router-link to="" class="button">edit</router-link>
            <button class="button" @click='delete_entity'>delete</button>
		</div>
        
    </div>
    <div>
        <table class="dashboard_table">
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
		</tr><tr v-for='(row,i) in dashboard_data' :key='i' class='data_rows'>
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
    dashboard_data: state => state.coaches.get_coaches_groupedby_all,
}),},
    methods: {
    call_request() {
    this.$store.dispatch("coaches/get_coaches_groupedby_all",
		 {
      });
    }
    }
    };
</script>
    