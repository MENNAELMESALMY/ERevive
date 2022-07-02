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
        <h2>dependent</h2>
        <div class="buttons">
            <router-link to="" class="button">Add +</router-link>
            <router-link to="" class="button">edit</router-link>
            <button class="button" @click='delete_entity'>delete</button>
		</div>
        
    </div>
    <div>
        <table class="dashboard_table">
        <tr v-if='dashboard_data.length>0'>
		<th>DEPENDENT relatlonship</th>
		<th>DEPENDENT name</th>
		<th>DEPENDENT birth date</th>
		<th>DEPENDENT sex</th>
		<th>DEPENDENT Dependents EMPLOYEE ssn</th>
		<th>count all</th>
		</tr><tr v-for='(row,i) in dashboard_data' :key='i' class='data_rows'>
			<td>{{row.DEPENDENT_relatlonship}}</td>
			<td>{{row.DEPENDENT_name}}</td>
			<td>{{row.DEPENDENT_birth_date}}</td>
			<td>{{row.DEPENDENT_sex}}</td>
			<td>{{row.DEPENDENT_Dependents_EMPLOYEE_ssn}}</td>
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
    dashboard_data: state => state.dependent.get_dependent_groupedby_all,
}),},
    methods: {
    call_request() {
    this.$store.dispatch("dependent/get_dependent_groupedby_all",
		 {
      });
    }
    }
    };
</script>
    