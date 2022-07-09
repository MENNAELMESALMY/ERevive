<template>
  <div class="showInfoTable">
    <table>
      <tr>
        <th>Name</th>
        <th>Number</th>
      </tr>

      <tr>
        <td>Primary Keys</td>
        <td>{{ primaryKeysCount }}</td>
      </tr>
      <tr>
        <td>Multivalued Attributes</td>
        <td>{{ multivaluedCount }}</td>
      </tr>
      <tr>
        <td>Identifying Relations</td>
        <td>{{ identifyingCount }}</td>
      </tr>
      <tr>
        <td>Weak Entities</td>
        <td>{{ weakEntitiesCount }}</td>
      </tr>
      <tr>
        <td>n-ary Relation</td>
        <td>{{ naryCount }}</td>
      </tr>
      <tr>
        <td>Full Participation</td>
        <td>{{ fullCount }}</td>
      </tr>
      <tr>
        <td>Partial Participation</td>
        <td>{{ partialCount }}</td>
      </tr>
    </table>
  </div>
</template>

<style lang="scss" scoped>
@import "../scss/Colors.scss";
table {
  width: 100%;
  border-collapse: collapse;
  border-spacing: 0;
  box-shadow: 0 2px 15px rgba(64, 64, 64, 0.7);
  border-radius: 12px 12px 0 0;
  overflow: hidden;
}
td,
th {
  padding: 15px 20px;
  text-align: center;
}
th {
  background-color: $darkBlue;
  color: white;
  font-weight: 700;
}
tr {
  width: 100%;
  background-color: white;
}
tr:nth-child(even) {
  background-color: #eeeeee;
}
</style>

<script>
export default {
  name: "showInfoTable",
  props: {
    primaryKeysCount: {
      type: Number,
      required: true,
    },
    multivaluedCount: {
      type: Number,
      required: true,
    },
    identifyingCount: {
      type: Number,
      required: true,
    },
    weakEntitiesCount: {
      type: Number,
      required: true,
    },
    naryCount: {
      type: Number,
      required: true,
    },
    fullCount: {
      type: Number,
      required: true,
    },
    partialCount: {
      type: Number,
      required: true,
    },
  },
};
</script>
