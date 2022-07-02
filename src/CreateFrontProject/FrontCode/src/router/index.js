
import { createWebHistory, createRouter } from "vue-router";
import home from "../views/home.vue";
import main_page from "../views/main_page.vue";
import create_writes__ from "../components/create_writes__.vue";
import get_posts_comments,__orderedby_all from "../components/get_posts_comments,__orderedby_all.vue";
import get_posts_comments,__filteredby__incrementalkey_groupedby_all from "../components/get_posts_comments,__filteredby__incrementalkey_groupedby_all.vue";
import get_posts_comments,__groupedby__incrementalkey_orderedby_all from "../components/get_posts_comments,__groupedby__incrementalkey_orderedby_all.vue";
import get_posts_comments,__groupedby_all_orderedby_all from "../components/get_posts_comments,__groupedby_all_orderedby_all.vue";
import get_writes__ from "../components/get_writes__.vue";
import get_posts_comments,__filteredby__incrementalkey_comments,_incrementalkey_groupedby__incrementalkey from "../components/get_posts_comments,__filteredby__incrementalkey_comments,_incrementalkey_groupedby__incrementalkey.vue";
import get_posts_comments,__groupedby_all from "../components/get_posts_comments,__groupedby_all.vue";
const routes = [
  {
    path: "/",
    name: "home",
    component: home,
  },
  {
    path: "/App",
    name: "App",
    component: main_page,
    children:[
    
        {
        
        path: "posts_comments,_/get_posts_comments,__filteredby__incrementalkey_groupedby_all",
        name: "get_posts_comments,__filteredby__incrementalkey_groupedby_all",
        component: get_posts_comments,__filteredby__incrementalkey_groupedby_all,
        
        },
        
        {
        
        path: "posts_comments,_/get_posts_comments,__groupedby_all",
        name: "get_posts_comments,__groupedby_all",
        component: get_posts_comments,__groupedby_all,
        
        },
        
        {
        
        path: "posts_comments,_/get_posts_comments,__groupedby_all_orderedby_all",
        name: "get_posts_comments,__groupedby_all_orderedby_all",
        component: get_posts_comments,__groupedby_all_orderedby_all,
        
        },
        
        {
        
        path: "posts_comments,_/get_posts_comments,__filteredby__incrementalkey_comments,_incrementalkey_groupedby__incrementalkey",
        name: "get_posts_comments,__filteredby__incrementalkey_comments,_incrementalkey_groupedby__incrementalkey",
        component: get_posts_comments,__filteredby__incrementalkey_comments,_incrementalkey_groupedby__incrementalkey,
        
        },
        
        {
        
        path: "posts_comments,_/get_posts_comments,__groupedby__incrementalkey_orderedby_all",
        name: "get_posts_comments,__groupedby__incrementalkey_orderedby_all",
        component: get_posts_comments,__groupedby__incrementalkey_orderedby_all,
        
        },
        
        {
        
        path: "posts_comments,_/get_posts_comments,__orderedby_all",
        name: "get_posts_comments,__orderedby_all",
        component: get_posts_comments,__orderedby_all,
        
        },
        
        {
        
        path: "writes__/get_writes__",
        name: "get_writes__",
        component: get_writes__,
        
        },
        
        {
        
        path: "writes__/create_writes__",
        name: "create_writes__",
        component: create_writes__,
        
        },
        
    ]
  }
];
        
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
    