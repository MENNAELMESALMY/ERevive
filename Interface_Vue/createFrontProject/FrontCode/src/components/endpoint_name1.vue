<template>
    <div class="dashboard">
        <div>		<label>course name</label>
		<input type="text" :v-model=course name>
		<label> regex matching (case invariant)</label>
		<label> max</label><br>
		<label>course id</label>
		<input type="number" :v-model=course id>
		<label> equal to</label>
		<label> avg</label><br>

        <input type="submit"
        value="Call endpoint"
        @click='call_request'>
        </div>
        <table>
        <tr>
		<th>field1</th>
		<th>field2</th>
		<th>field3</th>
		<th>field4</th>
		<th>field5</th>
		<th>field6</th>
		</tr><tr v-for='(row,i) in dashboard_data' :key='i'>
			<td>{{row.field1}}</td>
			<td>{{row.field2}}</td>
			<td>{{row.field3}}</td>
			<td>{{row.field4}}</td>
			<td>{{row.field5}}</td>
			<td>{{row.field6}}</td>
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
		course_name:"",
		course_id:"",

    };
    },
    computed: {
    ...mapState({
    dashboard_data: state => state.c1.endpoint_name1,
}),},
    methods: {
    call_request() {
    this.$store.dispatch("c1/endpoint_name1",
		 {course_name: this.course_name,
		course_id: this.course_id,
		
      });
    }
    }
    };
</script>
    