<template>
  <div class="dashboard">
    <div>
      <label>course name</label>
      <input type="text" :v-model="course" name />
      <label> regex matching (case invariant)</label>
      <label> max</label><br />
      <label>course id</label>
      <input type="number" :v-model="course" id />
      <label> equal to</label>
      <label> avg</label><br />

      <input type="submit" value="Call endpoint" />
    </div>
    <table>
      <tr>
        <th>field1</th>
        <th>field2</th>
      </tr>
      <tr v-for="(row, i) in dashboard_data" :key="i">
        <td>{{ row.field1 }}</td>
        <td>{{ row.field2 }}</td>
      </tr>
    </table>
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
      course_name: "",
      course_id: "",
    };
  },
  computed: {
    ...mapState({
      dashboard_data: (state) => state.cluster_name.endpoint_name,
    }),
  },
  methods: {
    call_request() {
      this.$store.dispatch("cluster_name/endpoint_name", {
        course_name: this.course_name,
        course_id: this.course_id,
      });
    },
  },
};
</script>
