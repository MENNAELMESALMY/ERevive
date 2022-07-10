const state = {
  predictedClusters: {
    Cluster1: [
      {
        name: "Query 1",
        query: "SELECT * FROM users",
      },
      {
        name: "Query 2",
        query:
          "select count ( * ) from class as t1 join enroll as t2 on t1.class_code = t2.class_code join course as t3 on t1.crs_code = t3.crs_code join department as t4 on t3.dept_code = t4.dept_code where t4.dept_name = 'accounting'",
      },
      {
        name: "Query 3",
        query:
          "select classes.id , count ( students_classes.* ) from students_classes join classes on students_classes.class_id = classes.id group by classes.id having count ( students_classes.* ) = 5",
      },
    ],
    Cluster2: [
      {
        name: "Query 4",
        query: "SELECT * FROM users",
      },
      {
        name: "Query 5",
        query:
          "select count ( * ) from class as t1 join enroll as t2 on t1.class_code = t2.class_code join course as t3 on t1.crs_code = t3.crs_code join department as t4 on t3.dept_code = t4.dept_code where t4.dept_name = 'accounting'",
      },
      {
        name: "Query 6",
        query:
          "select classes.id , count ( students_classes.* ) from students_classes join classes on students_classes.class_id = classes.id group by classes.id having count ( students_classes.* ) = 5",
      },
    ],
    Cluster3: [
      {
        name: "Query 7",
        query: "SELECT * FROM users",
      },
      {
        name: "Query 8",
        query:
          "select count ( * ) from class as t1 join enroll as t2 on t1.class_code = t2.class_code join course as t3 on t1.crs_code = t3.crs_code join department as t4 on t3.dept_code = t4.dept_code where t4.dept_name = 'accounting'",
      },
      {
        name: "Query 9",
        query:
          "select classes.id , count ( students_classes.* ) from students_classes join classes on students_classes.class_id = classes.id group by classes.id having count ( students_classes.* ) = 5",
      },
    ],
  },
  deletedQuery: "",
  deletedQueryName: "",
  clusters: ["Cluster1", "Cluster2", "Cluster3"],
  currentClusterName: "",
  queries: [],
};

const mutations = {
  setQueries(state, queriesList) {
    state.queries = queriesList;
  },
  setDeletedQuery(state, queryObject) {
    state.deletedQuery = queryObject.query;
    state.deletedQueryName = queryObject.queryName;
  },
  deleteQuery(state, queryObject) {
    state.queries = state.queries.filter(
      (item) =>
        item.name !== queryObject.queryName && item.query !== queryObject.query
    );
  },
  editQuery(state, queryObject) {
    state.queries.map((item) => {
      if (
        item.name == queryObject.oldQueryName &&
        item.query == queryObject.oldQuery
      ) {
        item.query = queryObject.query;
        item.name = queryObject.queryName;
      }
    });
  },
  addNewQuery(state, queryObject) {
    state.queries.push({
      name: queryObject.queryName,
      query: queryObject.query,
    });
  },
  setCurrentCluster(state, clusterName) {
    state.currentClusterName = clusterName;
    state.queries = state.predictedClusters[clusterName];
  },
};

export default {
  namespaced: true,
  state,
  mutations,
};
