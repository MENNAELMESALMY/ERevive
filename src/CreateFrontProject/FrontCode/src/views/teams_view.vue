
<template>
    <div>
    
      <get-teams/>
      
      <create-teams/>
      
    </div>
</template>

    <style lang="scss" scoped>
    .home {
    padding: 30px;
    }
    </style>

    <script>
    
      import getTeams from '../components/get_teams.vue'
      
      import createTeams from '../components/create_teams.vue'
      
export default {
  components: {
    
      getTeams,
      
      createTeams,
      
  },
};
</script>
    