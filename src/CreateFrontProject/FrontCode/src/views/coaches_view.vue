
<template>
    <div>
    
      <get-coaches-filteredby-coachID-groupedby-all/>
      
      <get-coaches-groupedby-all/>
      
      <get-coaches-filteredby-year-groupedby-coachID-year/>
      
      <get-coaches-groupedby-tmID-coachID-orderedby-all/>
      
      <get-coaches-groupedby-coachID-orderedby-all/>
      
      <get-coaches-groupedby-year-orderedby-all/>
      
      <get-coaches-filteredby-year/>
      
      <get-coaches-orderedby-all/>
      
    </div>
</template>

    <style lang="scss" scoped>
    .home {
    padding: 30px;
    }
    </style>

    <script>
    
      import getCoachesFilteredbyCoachidGroupedbyAll from '../components/get_coaches_filteredby_coachID_groupedby_all.vue'
      
      import getCoachesGroupedbyAll from '../components/get_coaches_groupedby_all.vue'
      
      import getCoachesFilteredbyYearGroupedbyCoachidYear from '../components/get_coaches_filteredby_year_groupedby_coachID_year.vue'
      
      import getCoachesGroupedbyTmidCoachidOrderedbyAll from '../components/get_coaches_groupedby_tmID_coachID_orderedby_all.vue'
      
      import getCoachesGroupedbyCoachidOrderedbyAll from '../components/get_coaches_groupedby_coachID_orderedby_all.vue'
      
      import getCoachesGroupedbyYearOrderedbyAll from '../components/get_coaches_groupedby_year_orderedby_all.vue'
      
      import getCoachesFilteredbyYear from '../components/get_coaches_filteredby_year.vue'
      
      import getCoachesOrderedbyAll from '../components/get_coaches_orderedby_all.vue'
      
export default {
  components: {
    
      getCoachesFilteredbyCoachidGroupedbyAll,
      
      getCoachesGroupedbyAll,
      
      getCoachesFilteredbyYearGroupedbyCoachidYear,
      
      getCoachesGroupedbyTmidCoachidOrderedbyAll,
      
      getCoachesGroupedbyCoachidOrderedbyAll,
      
      getCoachesGroupedbyYearOrderedbyAll,
      
      getCoachesFilteredbyYear,
      
      getCoachesOrderedbyAll,
      
  },
};
</script>
    