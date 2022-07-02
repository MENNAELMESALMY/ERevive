
<template>
  <div class="sideBar">
    <div class="header">
      <h4>Learning Management System</h4>
    </div>
  
    <ul class="clutsers">
      <li v-for="(card, i) in clustersNames" :key="i" class="cluster">
        <div class="clusterName" :title="card" :id="'clustersID' + i" @click="openClusterQueries('clustersID' + i,'queriesID' + i)">
           {{ card.substring(0, 19) + "..." }}
        </div>
        <ul class="queries" :id="'queriesID' + i">
          <li v-for="(item, j) in clusters[i]" :key="j" class="query">
            <router-link :to="'/App/' + card + '/' + item">
              <span class="queryName" :title="item">{{ item.substring(0, 19) + "..."}}</span>
            </router-link>
          </li>
        </ul>
      </li>
    </ul>
    <div class="footer">
      <h5>ERevive 2022</h5>
    </div>
  </div>
</template>

<script>
export default{
    data() {
        return {

        clustersNames: ['employee', 'dependent', 'department_location', 'works_employee_project', 'employee_department_location_department'],
        clusters: [['get_employee_filteredby_middle_name_last_name_groupedby_all', 'get_employee_filteredby_first_name_groupedby_all', 'get_employee_filteredby_last_name_groupedby_all_orderedby_salary', 'get_employee_filteredby_last_name_groupedby_all', 'get_employee_filteredby_last_name_orderedby_salary', 'get_employee_filteredby_sex_groupedby_all', 'get_employee_orderedby_status', 'get_employee_filteredby_salary_groupedby_all', 'get_employee_filteredby_middle_name', 'get_employee_groupedby_all', 'get_employee_groupedby_all_orderedby_birth_date', 'get_employee_filteredby_employee_supervision_ssn_groupedby_salary_middle_name_last_name_employee_supervision_ssn', 'get_employee_groupedby_salary_middle_name_last_name', 'get_employee_groupedby_salary_last_name_orderedby_all', 'get_employee_groupedby_middle_name_last_name_orderedby_all', 'get_employee_groupedby_last_name_employee_supervision_ssn_orderedby_all', 'get_employee_groupedby_last_name_orderedby_all', 'get_employee_filteredby_first_name_middle_name_last_name_groupedby_middle_name', 'get_employee_filteredby_last_name_birth_date_groupedby_employee_supervision_ssn_salary_birth_date', 'get_employee_filteredby_last_name_groupedby_birth_date', 'get_employee_filteredby_last_name_groupedby_birth_date_orderedby_employee_supervision_ssn', 'get_employee_filteredby_last_name_groupedby_birth_date_orderedby_salary', 'get_employee_filteredby_last_name_orderedby_employee_supervision_ssn', 'get_employee_filteredby_salary_groupedby_birth_date_salary_employee_supervision_ssn', 'get_employee_filteredby_salary_groupedby_birth_date_orderedby_birth_date', 'get_employee_filteredby_salary_groupedby_birth_date_orderedby_employee_supervision_ssn', 'get_employee_filteredby_salary_groupedby_birth_date_orderedby_salary', 'get_employee_filteredby_birth_date_groupedby_birth_date', 'get_employee_groupedby_birth_date_orderedby_employee_supervision_ssn', 'get_employee_filteredby_sex_salary', 'get_employee_groupedby_sex_orderedby_sex', 'get_employee_groupedby_sex_orderedby_all', 'get_employee_groupedby_address_orderedby_all', 'get_employee_filteredby_salary_orderedby_employee_supervision_ssn', 'get_employee_filteredby_salary_orderedby_salary', 'get_employee_groupedby_salary_orderedby_all', 'get_employee_orderedby_all', 'get_employee_groupedby_employee_supervision_ssn_orderedby_all'], ['get_dependent_groupedby_all', 'get_dependent_filteredby_sex'], ['get_department_location'], ['get_works_employee_project_filteredby_project_name_groupedby_all', 'get_works_employee_project_filteredby_project_name', 'get_works_employee_project_groupedby_all'], ['get_employee_department_location_department', 'get_employee_department_location_department_filteredby_department_name_groupedby_middle_name_address_department_name_last_name', 'get_employee_department_location_department_filteredby_department_name_groupedby_middle_name_last_name_department_name', 'get_employee_department_location_department_groupedby_department_name_orderedby_employee_supervision_ssn']],
        
        };
    },
    methods: {
    openClusterQueries(clusterid,queryid) {
      if (document.getElementById(queryid).style.display == "none"){
        document.getElementById(queryid).style.display = "block";
        document.getElementById(clusterid).style.backgroundColor = "rgba(200,206,206,0.1)";
        document.getElementById(clusterid).onmouseover = function() {
          document.getElementById(clusterid).style.backgroundColor = "rgba(200,206,206,0.1)";
        }
        document.getElementById(clusterid).onmouseout = function() {
          document.getElementById(clusterid).style.backgroundColor = "rgba(200,206,206,0.1)";
        }
      }else{
        document.getElementById(queryid).style.display = "none";
        document.getElementById(clusterid).style.backgroundColor = "#0f1136";
        document.getElementById(clusterid).onmouseover = function() {
          document.getElementById(clusterid).style.backgroundColor = "rgba(200,206,206,0.1)";
        }
        document.getElementById(clusterid).onmouseout = function() {
          document.getElementById(clusterid).style.backgroundColor = "#0f1136";
        }
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.sideBar {
  color: white;
  background-color: #0f1136;
  float: left;
  width: 230px;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  bottom: 0;
  padding: 0.5em;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  overflow-x: hidden;
  scrollbar-width: thin;
  scrollbar-color: #0f1136 #0f1136;
  &::-webkit-scrollbar {
    width: 1px;
  }
  &::-webkit-scrollbar-track {
    background-color: #0f1136;
  }
  &::-webkit-scrollbar-thumb {
    background-color: #0f1136;
  }
}
.header,
.footer {
  text-align: center;
  font-weight: 700;
}
.clutsers,
.queries {
  margin: 0;
  padding: 0;
}
.clutsers {
  padding-top: 20px;
}
.queries {
  margin-top: 15px;
  margin-bottom: 15px;
  display: none;
  transition: all 0.4s ease;
}
.cluster,
.query {
  margin: 0;
  padding: 0;
  padding-left: 5px;
  list-style: none;
  padding-top: 5px;
  padding-bottom: 10px;
  a {
    color: white;
    text-decoration: none;
    padding-left: 10px;
  }
}
.clusterName {
  font-size: 16px;
  font-weight: 700;
  color: white;
  padding-top: 15px;
  padding-bottom: 15px;
  padding-left: 5px;
  padding-right: 5px;
  width: 90%;
  cursor: pointer;
  &:hover {
    background-color: rgb(200, 206, 206, 0.1);
    border-radius: 7px;
  }
}
.query {
  padding-top: 12px;
  width: 90%;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  &:hover {
    background-color: rgb(200, 206, 206, 0.1);
  }
}
</style>
  