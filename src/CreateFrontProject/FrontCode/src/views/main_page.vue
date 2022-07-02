
<template>
    <div class="mainPage">
        <div class="content">
          <div class="sidebar">
            <sideBar />
          </div>
          <div class="rightContent">
          <router-view />
          </div>
        </div>
    </div>
</template>

<script>
import sideBar from '../components/sideBar.vue';
export default {
    name: "mainPage",
    components: {
        sideBar,
    }
};
</script>

<style lang="scss" scoped>
.content{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
.rightContent{
    padding-top: 20px;
    padding-bottom: 20px;
    width: calc(100% - 265px);
}
</style>
  