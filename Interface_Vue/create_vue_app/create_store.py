def generate_routing(clusters):
    routing_string = '''
import Vue from "vue";
import Vuex from "vuex";
'''
    for cluster in clusters:
        routing_string += 'import '+cluster+' from "./modules/'+cluster+'_store.vue";\n'
    routing_string += '''

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
'''
    for cluster in clusters:
        routing_string += '\t'+cluster + ',\n'
    routing_string +='''
  },
});'''
    return routing_string

clusters = ["employee","student","teacher","admin"]
create_dir = '../gpinterface/src/store/demo_index.js'
f = open(create_dir, "w")
f.write(generate_routing(clusters))
f.close()
