
<template>
    <div>
    
      <get-awards-coaches-series-post-coaches-filteredby-id/>
      
      <get-awards-coaches-series-post-coaches/>
      
    </div>
</template>

    <style lang="scss" scoped>
    .home {
    padding: 30px;
    }
    </style>

    <script>
    
      import getAwardsCoachesSeriesPostCoachesFilteredbyId from '../components/get_awards_coaches_series_post_coaches_filteredby_id.vue'
      
      import getAwardsCoachesSeriesPostCoaches from '../components/get_awards_coaches_series_post_coaches.vue'
      
export default {
  components: {
    
      getAwardsCoachesSeriesPostCoachesFilteredbyId,
      
      getAwardsCoachesSeriesPostCoaches,
      
  },
};
</script>
    