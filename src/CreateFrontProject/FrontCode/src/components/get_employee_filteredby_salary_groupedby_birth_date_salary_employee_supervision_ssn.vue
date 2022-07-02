<template>
    <div class="dashboard">
        <div class="sidebar">		<p>Filters</p>
		<form>
		<div class="filters">
		<div class="labels">
		<label> between</label>
		<label>EMPLOYEE_salary</label>
		</div>
		<div>
		<input type="number" v-model="EMPLOYEE_salary" class="number" required>
		</div>
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
		<th>EMPLOYEE EMPLOYEE Supervision ssn</th>
		<th>EMPLOYEE birth date</th>
		<th>EMPLOYEE salary</th>
		<th>avg EMPLOYEE EMPLOYEE Supervision ssn</th>
		<th>sum EMPLOYEE salary</th>
		<th>avg EMPLOYEE salary</th>
		<th>sum EMPLOYEE EMPLOYEE Supervision ssn</th>
		<th>count EMPLOYEE birth date</th>
		</tr><tr v-for='(row,i) in dashboard_data' :key='i' class='data_rows'>
			<td>{{row.EMPLOYEE_EMPLOYEE_Supervision_ssn}}</td>
			<td>{{row.EMPLOYEE_birth_date}}</td>
			<td>{{row.EMPLOYEE_salary}}</td>
			<td>{{row.avg_EMPLOYEE_EMPLOYEE_Supervision_ssn}}</td>
			<td>{{row.sum_EMPLOYEE_salary}}</td>
			<td>{{row.avg_EMPLOYEE_salary}}</td>
			<td>{{row.sum_EMPLOYEE_EMPLOYEE_Supervision_ssn}}</td>
			<td>{{row.count_EMPLOYEE_birth_date}}</td>
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
		EMPLOYEE_salary:"",

    };
    },
    computed: {
    ...mapState({
    dashboard_data: state => state.employee.get_employee_filteredby_salary_groupedby_birth_date_salary_employee_supervision_ssn,
}),},
    methods: {
    call_request() {
    this.$store.dispatch("employee/get_employee_filteredby_salary_groupedby_birth_date_salary_employee_supervision_ssn",
		 {'EMPLOYEE.salary': this.EMPLOYEE_salary,
		
      });
    }
    }
    };
</script>
    