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
        <h2>employee</h2>
        <div class="buttons">
            <router-link to="" class="button">Add +</router-link>
            <router-link to="" class="button">edit</router-link>
            <button class="button" @click='delete_entity'>delete</button>
		</div>
        
    </div>
    <div>
        <table class="dashboard_table">
        <tr v-if='dashboard_data.length>0'>
		<th>EMPLOYEE last name</th>
		<th>EMPLOYEE salary</th>
		<th>EMPLOYEE sex</th>
		<th>EMPLOYEE status</th>
		<th>EMPLOYEE DEPARTMENT Employed name</th>
		<th>EMPLOYEE middle name</th>
		<th>EMPLOYEE first name</th>
		<th>EMPLOYEE address</th>
		<th>EMPLOYEE birth date</th>
		<th>EMPLOYEE ssn</th>
		<th>EMPLOYEE start date</th>
		<th>EMPLOYEE EMPLOYEE Supervision ssn</th>
		<th>max EMPLOYEE birth date</th>
		<th>min EMPLOYEE salary</th>
		<th>min EMPLOYEE birth date</th>
		<th>max EMPLOYEE salary</th>
		<th>sum EMPLOYEE EMPLOYEE Supervision ssn</th>
		<th>avg EMPLOYEE EMPLOYEE Supervision ssn</th>
		<th>sum EMPLOYEE salary</th>
		<th>avg EMPLOYEE salary</th>
		<th>count all</th>
		</tr><tr v-for='(row,i) in dashboard_data' :key='i' class='data_rows'>
			<td>{{row.EMPLOYEE_last_name}}</td>
			<td>{{row.EMPLOYEE_salary}}</td>
			<td>{{row.EMPLOYEE_sex}}</td>
			<td>{{row.EMPLOYEE_status}}</td>
			<td>{{row.EMPLOYEE_DEPARTMENT_Employed_name}}</td>
			<td>{{row.EMPLOYEE_middle_name}}</td>
			<td>{{row.EMPLOYEE_first_name}}</td>
			<td>{{row.EMPLOYEE_address}}</td>
			<td>{{row.EMPLOYEE_birth_date}}</td>
			<td>{{row.EMPLOYEE_ssn}}</td>
			<td>{{row.EMPLOYEE_start_date}}</td>
			<td>{{row.EMPLOYEE_EMPLOYEE_Supervision_ssn}}</td>
			<td>{{row.max_EMPLOYEE_birth_date}}</td>
			<td>{{row.min_EMPLOYEE_salary}}</td>
			<td>{{row.min_EMPLOYEE_birth_date}}</td>
			<td>{{row.max_EMPLOYEE_salary}}</td>
			<td>{{row.sum_EMPLOYEE_EMPLOYEE_Supervision_ssn}}</td>
			<td>{{row.avg_EMPLOYEE_EMPLOYEE_Supervision_ssn}}</td>
			<td>{{row.sum_EMPLOYEE_salary}}</td>
			<td>{{row.avg_EMPLOYEE_salary}}</td>
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
    dashboard_data: state => state.employee.get_employee_groupedby_all,
}),},
    methods: {
    call_request() {
    this.$store.dispatch("employee/get_employee_groupedby_all",
		 {
      });
    }
    }
    };
</script>
    