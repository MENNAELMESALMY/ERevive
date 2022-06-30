def generate_store_idx(clusters,directory):
    store_string = '''
//import * as Vue from "vue";
import Vuex from "vuex";
'''
    for cluster in clusters:
        store_string += 'import '+cluster+' from "./modules/'+cluster+'.js";\n'
    store_string += '''

import color_pallete from "./modules/color_pallete.js";
//Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
'''
    for cluster in clusters:
        store_string += '\t'+cluster + ',\n'
    store_string +='''
    color_pallete
  },
});'''
    f = open(directory, "w")
    f.write(store_string)
    f.close()
