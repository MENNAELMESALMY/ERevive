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
        <h2>awards_coaches</h2>
        <div class="buttons">
            <router-link to="" class="button">Add +</router-link>
            <router-link to="" class="button">edit</router-link>
            <button class="button" @click='delete_entity'>delete</button>
		</div>
        
    </div>
    <div>
        <table class="dashboard_table">
        <tr>
		<th>awards coaches id</th>
		<th>awards coaches coachID</th>
		<th>awards coaches award</th>
		<th>awards coaches lgID</th>
		<th>awards coaches note</th>
		</tr><tr v-for='(row,i) in dashboard_data' :key='i' class='data_rows'>
			<td>{{row.awards_coaches_id}}</td>
			<td>{{row.awards_coaches_coachID}}</td>
			<td>{{row.awards_coaches_award}}</td>
			<td>{{row.awards_coaches_lgID}}</td>
			<td>{{row.awards_coaches_note}}</td>
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
    dashboard_data: state => state.awards_coaches.get_awards_coaches_filteredby_coachID_id,
}),},
    methods: {
    call_request() {
    this.$store.dispatch("awards_coaches/get_awards_coaches_filteredby_coachID_id",
		 {
      });
    }
    }
    };
</script>
    