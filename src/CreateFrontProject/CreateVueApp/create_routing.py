def generate_routing(clusters,clustersAndQueries,directory):
    routing_string = '''
import { createWebHistory, createRouter } from "vue-router";
import home from "../views/home.vue";
import main_page from "../views/main_page.vue";
'''
    imports = []
    for cluster in clusters:
      imports.append('import '+cluster+' from "../views/'+cluster+'_view.vue";')
    for queries in clustersAndQueries:
      for query in queries:
        imports.append('import '+query+' from "../components/'+query+'.vue";')
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
      path: "/{cluster}",
      name: "{cluster}",
      component: {cluster},
      children: [
      '''
      for query in clustersAndQueries[i]:
        routing_string += '''
        {
        '''
        routing_string += f'''
        path: "/{query}",
        name: "{query}",
        component: {query},
        '''
        routing_string += '''
        },
        '''
      i+=1
      routing_string += '''
      ]
  },
  '''
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

