
<template>
    <div>
    
      <get-awards-coaches-series-post-groupedby-all-orderedby-all/>
      
      <get-awards-coaches-series-post/>
      
      <get-awards-coaches-series-post-groupedby-coachID-id-orderedby-all/>
      
      <get-awards-coaches-series-post-groupedby-id/>
      
      <get-awards-coaches-series-post-groupedby-id-orderedby-all/>
      
    </div>
</template>

    <style lang="scss" scoped>
    .home {
    padding: 30px;
    }
    </style>

    <script>
    
      import getAwardsCoachesSeriesPostGroupedbyAllOrderedbyAll from '../components/get_awards_coaches_series_post_groupedby_all_orderedby_all.vue'
      
      import getAwardsCoachesSeriesPost from '../components/get_awards_coaches_series_post.vue'
      
      import getAwardsCoachesSeriesPostGroupedbyCoachidIdOrderedbyAll from '../components/get_awards_coaches_series_post_groupedby_coachID_id_orderedby_all.vue'
      
      import getAwardsCoachesSeriesPostGroupedbyId from '../components/get_awards_coaches_series_post_groupedby_id.vue'
      
      import getAwardsCoachesSeriesPostGroupedbyIdOrderedbyAll from '../components/get_awards_coaches_series_post_groupedby_id_orderedby_all.vue'
      
export default {
  components: {
    
      getAwardsCoachesSeriesPostGroupedbyAllOrderedbyAll,
      
      getAwardsCoachesSeriesPost,
      
      getAwardsCoachesSeriesPostGroupedbyCoachidIdOrderedbyAll,
      
      getAwardsCoachesSeriesPostGroupedbyId,
      
      getAwardsCoachesSeriesPostGroupedbyIdOrderedbyAll,
      
  },
};
</script>
    