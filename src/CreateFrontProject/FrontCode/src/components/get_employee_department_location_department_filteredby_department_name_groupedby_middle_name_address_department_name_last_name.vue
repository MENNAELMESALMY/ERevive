<template>
    <div class="dashboard">
        <div class="sidebar">		<p>Filters</p>
		<form>
		<div class="filters">
		<div class="labels">
		<label> regex matching (case invariant)</label>
		<label>DEPARTMENT_location_DEPARTMENT_name</label>
		</div>
		<div>
		<input type="text" v-model="DEPARTMENT_location_DEPARTMENT_name" class="text" required>
		</div>
		<div class="labels">
		<label> equal to</label>
		<label>DEPARTMENT_location_DEPARTMENT_name</label>
		</div>
		<div>
		<input type="text" v-model="DEPARTMENT_location_DEPARTMENT_name" class="text" required>
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
        <h2>employee_department_location_department</h2>
    </div>
    <div>
        <table class="dashboard_table">
        <tr v-if='dashboard_data.length>0'>
		<th>DEPARTMENT location DEPARTMENT name</th>
		<th>EMPLOYEE last name</th>
		<th>EMPLOYEE middle name</th>
		<th>EMPLOYEE address</th>
		<th>sum EMPLOYEE EMPLOYEE Supervision ssn</th>
		</tr><tr v-for='(row,i) in dashboard_data' :key='i' class='data_rows'>
			<td>{{row.DEPARTMENT_location_DEPARTMENT_name}}</td>
			<td>{{row.EMPLOYEE_last_name}}</td>
			<td>{{row.EMPLOYEE_middle_name}}</td>
			<td>{{row.EMPLOYEE_address}}</td>
			<td>{{row.sum_EMPLOYEE_EMPLOYEE_Supervision_ssn}}</td>
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
		DEPARTMENT_location_DEPARTMENT_name:"",
		DEPARTMENT_location_DEPARTMENT_name:"",

    };
    },
    computed: {
    ...mapState({
    dashboard_data: state => state.employee_department_location_department.get_employee_department_location_department_filteredby_department_name_groupedby_middle_name_address_department_name_last_name,
}),},
    methods: {
    call_request() {
    this.$store.dispatch("employee_department_location_department/get_employee_department_location_department_filteredby_department_name_groupedby_middle_name_address_department_name_last_name",
		 {'DEPARTMENT_location.DEPARTMENT_name': this.DEPARTMENT_location_DEPARTMENT_name,
		'DEPARTMENT_location.DEPARTMENT_name': this.DEPARTMENT_location_DEPARTMENT_name,
		
      });
    }
    }
    };
</script>
    