def generate_routing(clusters,clustersAndQueries,directory):
    routing_string = '''
import { createWebHistory, createRouter } from "vue-router";
import home from "../views/home.vue";
import main_page from "../views/main_page.vue";
'''
    imports = []
    for cluster in clusters:
      imports.append('import '+cluster+' from "../views/'+cluster+'.vue";')
    for queries in clustersAndQueries:
      for query in queries:
        if query['method'] == 'delete': continue
        imports.append('import '+query['endpoint_name']+' from "../components/'+query['endpoint_name']+'.vue";')
    imports = list(set(imports))
    routing_string += "\n".join(imports)
    routing_string += '''
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
    '''
    i = 0
    for cluster in clusters:
      routing_string += '''
        {
        '''
      routing_string += f'''
        path: "{cluster}",
        name: "{cluster}",
        component: {cluster},
        '''
      routing_string += '''
        },
        '''
      for fullQuery in clustersAndQueries[i]:
        if fullQuery['method'] == 'delete': continue
        query = fullQuery['endpoint_name']
        routing_string += '''
        {
        '''
        if fullQuery['method'] == 'put':
          routing_string += f'''
          path: "{cluster}_{query}/:id",
          name: "{query}",
          component: {query},
          '''
        else:
          routing_string += f'''
          path: "{cluster}_{query}",
          name: "{query}",
          component: {query},
          '''

        routing_string += '''
        },
        '''
      i+=1
    routing_string += '''
    ]
  }
];
        
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
    '''
    f = open(directory, "w")
    f.write(routing_string)
    f.close()

