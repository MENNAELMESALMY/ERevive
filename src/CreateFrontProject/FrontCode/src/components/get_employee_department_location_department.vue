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
        <h2>employee_department_location_department</h2>
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
		<th>DEPARTMENT location DEPARTMENT name</th>
		<th>DEPARTMENT location Clocation</th>
		<th>DEPARTMENT location location</th>
		<th>DEPARTMENT name</th>
		<th>DEPARTMENT start date</th>
		<th>DEPARTMENT EMPLOYEE Manages ssn</th>
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
			<td>{{row.DEPARTMENT_location_DEPARTMENT_name}}</td>
			<td>{{row.DEPARTMENT_location_Clocation}}</td>
			<td>{{row.DEPARTMENT_location_location}}</td>
			<td>{{row.DEPARTMENT_name}}</td>
			<td>{{row.DEPARTMENT_start_date}}</td>
			<td>{{row.DEPARTMENT_EMPLOYEE_Manages_ssn}}</td>
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
    dashboard_data: state => state.employee_department_location_department.get_employee_department_location_department,
}),},
    methods: {
    call_request() {
    this.$store.dispatch("employee_department_location_department/get_employee_department_location_department",
		 {
      });
    }
    }
    };
</script>
    