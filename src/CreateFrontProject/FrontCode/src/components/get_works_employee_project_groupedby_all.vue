<template>
    <div class="dashboard">
        <div class="sidebar">		<form>
		<div class="filters">
		</div>

        <input type="submit"
        value="Call endpoint"
        class="button"
        @click='call_request'>
        </form>
        </div>

<div class="content">
        <div class="table_nav">
        <h2>works_employee_project</h2>
        <div class="buttons">
            <router-link to="" class="button">Add +</router-link>
            <router-link to="" class="button">edit</router-link>
            <button class="button" @click='delete_entity'>delete</button>
		</div>
        
    </div>
    <div>
        <table class="dashboard_table">
        <tr v-if='dashboard_data.length>0'>
		<th>Works EMPLOYEE PROJECT start date</th>
		<th>Works EMPLOYEE PROJECT hours</th>
		<th>Works EMPLOYEE PROJECT EMPLOYEE ssn</th>
		<th>Works EMPLOYEE PROJECT PROJECT name</th>
		<th>count all</th>
		</tr><tr v-for='(row,i) in dashboard_data' :key='i' class='data_rows'>
			<td>{{row.Works_EMPLOYEE_PROJECT_start_date}}</td>
			<td>{{row.Works_EMPLOYEE_PROJECT_hours}}</td>
			<td>{{row.Works_EMPLOYEE_PROJECT_EMPLOYEE_ssn}}</td>
			<td>{{row.Works_EMPLOYEE_PROJECT_PROJECT_name}}</td>
			<td>{{row.count_all}}</td>
		</tr>
        </table>
        </div>
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
    dashboard_data: state => state.works_employee_project.get_works_employee_project_groupedby_all,
}),},
    methods: {
    call_request() {
    this.$store.dispatch("works_employee_project/get_works_employee_project_groupedby_all",
		 {
      });
    }
    }
    };
</script>
    