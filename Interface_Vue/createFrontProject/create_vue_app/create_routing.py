def generate_routing(clusters,directory):
    routing_string = '''
import { createWebHistory, createRouter } from "vue-router";
import home from "../views/home.vue";
import main_page from "../views/main_page.vue";
'''
    imports = []
    for cluster in clusters:
         imports.append('import '+cluster+' from "../views/'+cluster+'_view.vue";')
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
    component: main_page
	},
'''
    for cluster in clusters:
        routing_string += '\n\t\t{\n\t\tpath: "/'+cluster\
            +'",\n\t\tname: "'+cluster\
            +'",\n\t\tcomponent: '+cluster\
            +'\n\t\t},\n'
    routing_string +='''
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

