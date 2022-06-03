def generate_store(endpoints,directory):
    store_string = '''
import axios from "axios";
import router from "@/router";
const state = {
  '''
    for endpoint in endpoints:
        store_string += endpoint["endpoint_name"] + ':' + '[],'
     
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
            print('get')
            store_string += '\t\t\tparams: payload.query_param,'
        if endpoint['method'] == 'post' or endpoint['method'] == 'put':
            print('post')
            store_string += '\t\t\tdata: payload.body_param,'
        
        store_string += '})\n'
        
        if endpoint['method'] == 'get':
            store_string += '\t\t\tstate.'+endpoint["endpoint_name"]+' = response.data;\n'
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