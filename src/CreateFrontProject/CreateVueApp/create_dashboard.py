def generate_dashboard(cluster_name,endpoint,directory,
    is_single_entity=False,delete_route='',put_route='',post_route=''):

    table_headers_orig = list(endpoint['response'].keys())

    table_headers = [header.replace('.',' ').replace('_',' ')  for header in table_headers_orig]
    table_headers_orig = [header.replace('.','_').replace('_','_')  for header in table_headers_orig]

    # cluster_name = endpoint['cluster_name']
    endpoint_name = endpoint['endpoint_name']
    query_params = [(param,d,o,a) for param,d,o,a in endpoint['queryParams']]
    dashboard_string = '''<template>
    <div class="dashboard">
        <div class="sidebar">'''
        
    dashboard_string += '\t\t<p>Filters</p>\n'
    dashboard_string += '\t\t<div class="filters">\n'
    for param,datatype,operator,aggregate in query_params:
        param = param.replace('.','_')
        if operator == '<':operator = 'less than'
        elif operator == '>':operator = 'greater than'
        elif operator == '=' or operator == 'is':operator = 'equal to'
        elif operator == '!=':operator = 'not equal to'
        elif operator == '<=':operator = 'less than or equal to'
        elif operator == '>=':operator = 'greater than or equal to'
        elif operator == 'like':operator = 'regex matching (case invariant)'
        elif operator == 'not like':operator = 'regex matching (case invariant)'
        if not operator: operator = 'equal to'

        if datatype == 'str':datatype = 'text'
        elif datatype == 'int' or datatype == 'float':datatype = 'number'
        elif datatype=='bool':datatype = 'checkbox'
        elif datatype == 'date':datatype = 'date'
        else: datatype = 'text'

        dashboard_string += '\t\t<div>\n'
        if aggregate: dashboard_string += '\t\t<label> '+ aggregate+'</label><br>\n'
        dashboard_string += '\t\t<label> '+ operator +'</label>\n'
        dashboard_string += '\t\t<label>'+ param +'</label>\n'
        dashboard_string += '\t\t</div>\n'

        dashboard_string += '\t\t<div>\n'
        dashboard_string += '\t\t<input type="'+datatype+'" v-model="'+param+'">\n'
        dashboard_string += '\t\t</div>\n'

    dashboard_string += '\t\t</div>\n'  

    dashboard_string +='''
        <input type="submit"
        value="Call endpoint"
        class="button"
        @click='call_request'>
        </div>

        <div class="table_nav">
        '''
    dashboard_string += '<h2>'+cluster_name+'</h2>'
    if is_single_entity:
        dashboard_string += f'''
        <div class="buttons">
            <router-link to="{post_route}" class="button">Add +</router-link>
            <router-link to="{put_route}" class="button">edit</router-link>
            <button class="button" @click='delete_entity'>delete</button>
		</div>
        '''
    dashboard_string +=    '''
    </div>
    <div>
        <table class="dashboard_table">
        <tr>\n'''
    for header in table_headers:
        dashboard_string += '\t\t<th>' + header + '</th>\n'
    dashboard_string += '\t\t</tr>'
    dashboard_string +=  "<tr v-for='(row,i) in dashboard_data' :key='i' class='data_rows'>\n"
    for header in table_headers_orig:
        dashboard_string += '\t\t\t<td>{{row.' + header + '}}</td>\n'
    dashboard_string += '\t\t</tr>'
    dashboard_string += '''
        </table>
        </div>
    </div>
</template>

<style lang="scss" scoped>
@import "../scss/dashboard.scss";
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
        dashboard_string += '\t\t'+param.replace('.','_').replace(' ','_') + ':' + '"",\n'
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
        dashboard_string += "'"+param+"'" +': this.' + param.replace('.','_').replace(' ','_') + ',\n\t\t'

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