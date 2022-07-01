
<template>
    <div>
    
      <get-coaches-awards-coaches-filteredby-year/>
      
      <get-awards-coaches-coaches-groupedby-coachID/>
      
      <get-awards-coaches-coaches-orderedby-all/>
      
    </div>
</template>

    <style lang="scss" scoped>
    .home {
    padding: 30px;
    }
    </style>

    <script>
    
      import getCoachesAwardsCoachesFilteredbyYear from '../components/get_coaches_awards_coaches_filteredby_year.vue'
      
      import getAwardsCoachesCoachesGroupedbyCoachid from '../components/get_awards_coaches_coaches_groupedby_coachID.vue'
      
      import getAwardsCoachesCoachesOrderedbyAll from '../components/get_awards_coaches_coaches_orderedby_all.vue'
      
export default {
  components: {
    
      getCoachesAwardsCoachesFilteredbyYear,
      
      getAwardsCoachesCoachesGroupedbyCoachid,
      
      getAwardsCoachesCoachesOrderedbyAll,
      
  },
};
</script>
    