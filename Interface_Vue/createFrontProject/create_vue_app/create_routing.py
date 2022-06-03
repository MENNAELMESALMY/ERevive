def generate_routing(clusters,directory):
    routing_string = '''
import Vue from "vue";
import VueRouter from "vue-router";
import home from "../views/home_view.vue";
'''
    for cluster in clusters:
        routing_string += 'import '+cluster+' from "../views/'+cluster+'_view.vue";\n'
    routing_string += '''

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: home,
    children: [
'''
    for cluster in clusters:
        routing_string += '\n\t\t{\n\t\tpath: "'+cluster\
            +'/",\n\t\tname: "'+cluster\
            +'",\n\t\tcomponent: '+cluster\
            +'\n\t\t},\n'
    routing_string +='''
    ]
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
    '''
    f = open(directory, "w")
    f.write(routing_string)
    f.close()

