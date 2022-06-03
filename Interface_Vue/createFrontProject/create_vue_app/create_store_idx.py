def generate_store_idx(clusters,directory):
    store_string = '''
import Vue from "vue";
import Vuex from "vuex";
'''
    for cluster in clusters:
        store_string += 'import '+cluster+' from "./modules/'+cluster+'_store.vue";\n'
    store_string += '''

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
'''
    for cluster in clusters:
        store_string += '\t'+cluster + ',\n'
    store_string +='''
  },
});'''
    f = open(directory, "w")
    f.write(store_string)
    f.close()
