def generate_dashboard(cluster_name,endpoint,directory):
    table_headers = list(endpoint['response'].keys())
    table_headers = [header.replace('.',' ').replace('_',' ')  for header in table_headers]
    # cluster_name = endpoint['cluster_name']
    endpoint_name = endpoint['endpoint_name']
    query_params = [(param.replace('.',' ').replace('_',' '),d,o,a) for param,d,o,a in endpoint['query_params']]
    dashboard_string = '''<template>
    <div class="dashboard">
        <div>'''
    for param,datatype,operator,aggregate in query_params:
        dashboard_string += '\t\t<label>'+ param +'</label>\n'
        if datatype == 'str':datatype = 'text'
        elif datatype == 'int' or datatype == 'float':datatype = 'number'
        elif datatype=='bool':datatype = 'checkbox'
        elif datatype == 'date':datatype = 'date'
        else: datatype = 'text'

        if operator == '<':operator = 'less than'
        elif operator == '>':operator = 'greater than'
        elif operator == '=' or operator == 'is':operator = 'equal to'
        elif operator == '!=':operator = 'not equal to'
        elif operator == '<=':operator = 'less than or equal to'
        elif operator == '>=':operator = 'greater than or equal to'
        elif operator == 'like':operator = 'regex matching (case invariant)'
        elif operator == 'not like':operator = 'regex matching (case invariant)'

        dashboard_string += '\t\t<input type="'+datatype+'" :v-model='+param+'>\n'
        dashboard_string += '\t\t<label> '+ operator +'</label>\n'
        dashboard_string += '\t\t<label> '+ aggregate +'</label><br>\n'

    dashboard_string +='''
        <input type="submit"
        value="Call endpoint"
        @click='call_request'>
        </div>
        <table>
        <tr>\n'''
    for header in table_headers:
        dashboard_string += '\t\t<th>' + header + '</th>\n'
    dashboard_string += '\t\t</tr>'
    dashboard_string +=  "<tr v-for='(row,i) in dashboard_data' :key='i'>\n"
    for header in table_headers:
        dashboard_string += '\t\t\t<td>{{row.' + header + '}}</td>\n'
    dashboard_string += '\t\t</tr>'
    dashboard_string += '''
        </table>
    </div>
</template>

<style lang="scss" scoped>
// @import "../scss/dashboard.scss";
</style>

<script>
    import { mapState } from "vuex";
    export default {
    name: "dashBoard",
    props: {},
    data: function () {
    return {
'''
    for param,_,_,_ in query_params:
        dashboard_string += '\t\t'+param.replace(' ','_') + ':' + '"",\n'
    dashboard_string += '''
    };
    },
    computed: {
    ...mapState({
    '''
    dashboard_string += 'dashboard_data: state => state.'\
                    +cluster_name+'.'+endpoint_name+',\n'
    dashboard_string += '''}),},
    methods: {
    call_request() {
    '''
    dashboard_string+= 'this.$store.dispatch("'+cluster_name +'/'+endpoint_name +'",\n\t\t {'
    for param,_,_,_ in query_params:
        param = param.replace(' ','_')
        dashboard_string += param +': this.' + param + ',\n\t\t'

    dashboard_string += '''
      });
    }
    }
    };
</script>
    '''
    f = open(directory, "w")
    f.write(dashboard_string)
    f.close()

# test_endpoint = {
#     'url':'',
#     'method':'get',
#     'query_params':[('course_name','str','like','max'),('course_id','int','=','avg')],
#     'body_params':['name','bday'],
#     'path_params':['course_path'],
#     'response':{'field1':'value1', 'field2':'value2'},
#     'cluster_name':'cluster_name',
#     'ui_name':'ui_name',
#     'endpoint_name':'endpoint_name',
# }

# create_dir = '../gpinterface/src/components/'+test_endpoint['endpoint_name']+'.vue'
# f = open(create_dir, "w")
# f.write(generate_dashboard(test_endpoint))
# f.close()