
<template>
    <div>
    
      <get-awards-coaches/>
      
      <get-awards-coaches-filteredby-coachID-id/>
      
    </div>
</template>

    <style lang="scss" scoped>
    .home {
    padding: 30px;
    }
    </style>

    <script>
    
      import getAwardsCoaches from '../components/get_awards_coaches.vue'
      
      import getAwardsCoachesFilteredbyCoachidId from '../components/get_awards_coaches_filteredby_coachID_id.vue'
      
export default {
  components: {
    
      getAwardsCoaches,
      
      getAwardsCoachesFilteredbyCoachidId,
      
  },
};
</script>
    