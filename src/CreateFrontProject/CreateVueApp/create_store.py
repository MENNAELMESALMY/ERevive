def generate_store(endpoints,directory):
    store_string = '''
import axios from "axios";
const state = {
'''
    for endpoint in endpoints:
        store_string += '\t\t'+endpoint["endpoint_name"] + ':' + '[],\n'
     
    store_string += '''
};

const actions = {
'''
    for endpoint in endpoints:
        store_string += '\t\tasync '+endpoint["endpoint_name"] + '({ state }, payload) {\n'
        store_string += '\t\ttry{\n\t\t\tconst response = await axios({'
        store_string += '\n\t\t\tmethod: "'+endpoint["method"]+'",\n'
        store_string += '\t\t\turl: "'+endpoint["url"]+'",\n'
        #print(endpoint['method'])
        if endpoint['method'] == 'get' or endpoint['method']=='delete':
            store_string += '\t\t\tparams: payload,'
        if endpoint['method'] == 'post' or endpoint['method'] == 'put':
            store_string += '\t\t\tdata: payload.body_param,'
        
        store_string += '})\n'
        
        if endpoint['method'] == 'get':
            store_string += '''
            let results = response.data
            let store_data = []
            for (let i = 0; i < results.length; i++) {
                let item = results[i]
                let store_item = {}
                for (let key in item) {
                    store_item[key.replace('.','_').replace(' ','_')] = item[key]
                }
                store_data.push(store_item)
            }
            '''
            store_string += '\t\t\tstate.'+endpoint["endpoint_name"]+' = store_data;\n'
        store_string += '\t\t} catch (error) {\n\t\t\tconsole.log(error)\n\t\t}},\n'

    store_string += '''
    };

export default {
  namespaced: true,
  state,
  actions,
};
    '''
    f = open(directory, "w")
    f.write(store_string)
    f.close()